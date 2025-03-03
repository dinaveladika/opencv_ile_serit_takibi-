#include <behaviortree_cpp_v3/bt_factory.h>
#include "detect_obstacle_node.cpp"
#include "stop_robot_node.cpp"

int main()
{
    BT::BehaviorTreeFactory factory;

    factory.registerNodeType<DetectObstacle>("DetectObstacle");
    factory.registerNodeType<StopRobot>("StopRobot");

    auto tree = factory.createTreeFromFile("my_tree.xml");

    while (true)
    {
        tree.tickRoot();
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }

    return 0;
}
