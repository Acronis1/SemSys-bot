from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.knowledge_base.utils import (
    SLOT_OBJECT_TYPE,
    SLOT_LAST_OBJECT_TYPE,
    SLOT_ATTRIBUTE,
    reset_attribute_slots,
    SLOT_MENTION,
    SLOT_LAST_OBJECT,
    SLOT_LISTED_OBJECTS,
    get_object_name,
    get_attribute_slots,
)
from typing import Text, Callable, Dict, List, Any, Optional
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.interfaces import Tracker
from rasa_sdk.knowledge_base.storage import KnowledgeBase
import urllib

class ActionMyKB(ActionQueryKnowledgeBase):
    def __init__(self):
        # load knowledge base with data from the given file
        knowledge_base = InMemoryKnowledgeBase("knowledge_base_data.json")

        # overwrite the representation function of the hotel object
        # by default the representation function is just the name of the object
        knowledge_base.set_representation_function_of_object(
            "hotel", lambda obj: obj["name"] + " (" + obj["city"] + ")"
        )

        super().__init__(knowledge_base)
    
    def utter_attribute_value(
        self,
        dispatcher: CollectingDispatcher,
        object_name: Text,
        attribute_name: Text,
        attribute_value: Text,
        custom=False,
        load=None,
    ) -> None:
        """
        Utters a response that informs the user about the attribute value of the
        attribute of interest.
        Args:
            dispatcher: the dispatcher
            object_name: the name of the object
            attribute_name: the name of the attribute
            attribute_value: the value of the attribute
        """
        if custom == False:
            if attribute_value:
                print(attribute_name)
                print(type(attribute_name))
                dispatcher.utter_message(
                    text=f"'{object_name}' has the value custom '{attribute_value}' for attribute '{attribute_name}'."
                )
            else:
                dispatcher.utter_message(
                    text=f"Did not find a valid value for attribute '{attribute_name}' for object '{object_name}'."
               )
        else:
            my_dict = {"text": "Click here to open the website", "buttons": [ {"title": "Click me", "payload": load}]}
            dispatcher.utter_message(text="Sure thing, here you go: \n")
            dispatcher.utter_message(text=load)

    


    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        """
        Executes this action. If the user ask a question about an attribute,
        the knowledge base is queried for that attribute. Otherwise, if no
        attribute was detected in the request or the user is talking about a new
        object type, multiple objects of the requested type are returned from the
        knowledge base.
        Args:
            dispatcher: the dispatcher
            tracker: the tracker
            domain: the domain
        Returns: list of slots
        """
        object_type = tracker.get_slot(SLOT_OBJECT_TYPE)
        last_object_type = tracker.get_slot(SLOT_LAST_OBJECT_TYPE)
        attribute = tracker.get_slot(SLOT_ATTRIBUTE)

        new_request = object_type != last_object_type

        if not object_type:
            # object type always needs to be set as this is needed to query the
            # knowledge base
            dispatcher.utter_message(template="utter_ask_rephrase")
            return []

        if not attribute or new_request:
            return self._query_objects(dispatcher, tracker)
        elif attribute:
            return self._query_attribute(dispatcher, tracker)

        dispatcher.utter_message(template="utter_ask_rephrase")
        return []

    def _query_objects(
        self, dispatcher: CollectingDispatcher, tracker: Tracker
    ) -> List[Dict]:
        """
        Queries the knowledge base for objects of the requested object type and
        outputs those to the user. The objects are filtered by any attribute the
        user mentioned in the request.
        Args:
            dispatcher: the dispatcher
            tracker: the tracker
        Returns: list of slots
        """
        object_type = tracker.get_slot(SLOT_OBJECT_TYPE)
        object_attributes = self.knowledge_base.get_attributes_of_object(object_type)

        # get all set attribute slots of the object type to be able to filter the
        # list of objects
        attributes = get_attribute_slots(tracker, object_attributes)
        # query the knowledge base
        objects = self.knowledge_base.get_objects(object_type, attributes)

        self.utter_objects(dispatcher, object_type, objects)

        if not objects:
            return reset_attribute_slots(tracker, object_attributes)

        key_attribute = self.knowledge_base.get_key_attribute_of_object(object_type)

        last_object = None if len(objects) > 1 else objects[0][key_attribute]

        slots = [
            SlotSet(SLOT_OBJECT_TYPE, object_type),
            SlotSet(SLOT_MENTION, None),
            SlotSet(SLOT_ATTRIBUTE, None),
            SlotSet(SLOT_LAST_OBJECT, last_object),
            SlotSet(SLOT_LAST_OBJECT_TYPE, object_type),
            SlotSet(
                SLOT_LISTED_OBJECTS, list(map(lambda e: e[key_attribute], objects))
            ),
        ]

        return slots + reset_attribute_slots(tracker, object_attributes)

    def _query_attribute(
        self, dispatcher: CollectingDispatcher, tracker: Tracker
    ) -> List[Dict]:
        """
        Queries the knowledge base for the value of the requested attribute of the
        mentioned object and outputs it to the user.
        Args:
            dispatcher: the dispatcher
            tracker: the tracker
        Returns: list of slots
        """
        object_type = tracker.get_slot(SLOT_OBJECT_TYPE)
        attribute = tracker.get_slot(SLOT_ATTRIBUTE)




        object_name = get_object_name(
            tracker,
            self.knowledge_base.ordinal_mention_mapping,
            self.use_last_object_mention,
        )

        if not object_name or not attribute:
            dispatcher.utter_message(template="utter_ask_rephrase")
            return [SlotSet(SLOT_MENTION, None)]

        object_of_interest = self.knowledge_base.get_object(object_type, object_name)


        if attribute in ["address", "latitude", "longitude", "url"] :

            base = "https://www.google.com/maps/search/?api=1&query="
 
            url = base + urllib.parse.quote(object_of_interest["name"])

            value = object_of_interest[attribute]
            repr_function = self.knowledge_base.get_representation_function_of_object(
                object_type
            )
            object_representation = repr_function(object_of_interest)
            
            self.utter_attribute_value(dispatcher, object_representation, attribute, value, custom=True, load=url)

            key_attribute = self.knowledge_base.get_key_attribute_of_object(object_type)
            object_identifier = object_of_interest[key_attribute]

            slots = [
                SlotSet(SLOT_OBJECT_TYPE, object_type),
                SlotSet(SLOT_ATTRIBUTE, None),
                SlotSet(SLOT_MENTION, None),
                SlotSet(SLOT_LAST_OBJECT, object_identifier),
                SlotSet(SLOT_LAST_OBJECT_TYPE, object_type),
            ]

            return slots
        else:

            if not object_of_interest or attribute not in object_of_interest:
                dispatcher.utter_message(template="utter_ask_rephrase")
                return [SlotSet(SLOT_MENTION, None)]

            value = object_of_interest[attribute]
            repr_function = self.knowledge_base.get_representation_function_of_object(
                object_type
            )
            object_representation = repr_function(object_of_interest)
            key_attribute = self.knowledge_base.get_key_attribute_of_object(object_type)
            object_identifier = object_of_interest[key_attribute]

            self.utter_attribute_value(dispatcher, object_representation, attribute, value)

            slots = [
                SlotSet(SLOT_OBJECT_TYPE, object_type),
                SlotSet(SLOT_ATTRIBUTE, None),
                SlotSet(SLOT_MENTION, None),
                SlotSet(SLOT_LAST_OBJECT, object_identifier),
                SlotSet(SLOT_LAST_OBJECT_TYPE, object_type),
            ]

            return slots

 