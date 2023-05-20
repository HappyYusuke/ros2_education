import time
import rclpy
from rclpy.node import Node
import smach


class SearchPerson(smach.State):
    def __init__(self, _node):
        smach.State.__init__(self, outcomes=['person', 'none_person'])
        self.counter = 0
        self.logger = _node.get_logger()

    def execute(self, userdata):
        self.logger.info("Searching ...")
        time.sleep(1.0)
        if self.counter < 3:
            self.logger.info("Person is here !")
            self.counter += 1
            return 'person'
        else:
            self.logger.info("person is not here ...")
            return 'none_person'


class SayHello(smach.State):
    def __init__(self, _node):
        smach.State.__init__(self, outcomes=['said_hello'])
        self.logger = _node.get_logger()

    def execute(self, userdata):
        self.logger.info("Heeeeeeeeeeeeelloooooooooooooooo!")
        time.sleep(0.5)
        return 'said_hello'


class StateMachine(Node):
    def __init__(self):
        super().__init__('simple_sm')

    def execute(self):
        # Smachでステートマシーンを宣言
        sm = smach.StateMachine(outcomes=['end'])
        # コンテナを開く
        with sm:
            # 状態を追加
            smach.StateMachine.add(
                    'SEARCH_PERSON', SearchPerson(self),
                    transitions={'person': 'SAY_HELLO', 'none_person': 'end'})
            smach.StateMachine.add(
                    'SAY_HELLO', SayHello(self),
                    transitions={'said_hello': 'SEARCH_PERSON'})

        # 実行
        outcome = sm.execute()
        self.get_logger().info(f"outcom: {outcome}")


def main():
    rclpy.init()
    node = StateMachine()
    node.execute()
