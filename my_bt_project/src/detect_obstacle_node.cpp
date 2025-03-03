#include <behaviortree_cpp_v3/action_node.h>
#include <sensor_msgs/msg/image.hpp>
#include <rclcpp/rclcpp.hpp>

class DetectObstacle : public BT::SyncActionNode
{
public:
    DetectObstacle(const std::string &name, const BT::NodeConfiguration &config)
        : BT::SyncActionNode(name, config)
    {
        node_ = rclcpp::Node::make_shared("detect_obstacle_node");
        subscription_ = node_->create_subscription<sensor_msgs::msg::Image>(
            "/camera/image_raw", 10,
            std::bind(&DetectObstacle::imageCallback, this, std::placeholders::_1));
    }

    static BT::PortsList providedPorts()
    {
        return {};
    }

    BT::NodeStatus tick() override
    {
        if (obstacle_detected_)
        {
            return BT::NodeStatus::SUCCESS;
        }
        return BT::NodeStatus::FAILURE;
    }

private:
    rclcpp::Node::SharedPtr node_;
    rclcpp::Subscription<sensor_msgs::msg::Image>::SharedPtr subscription_;
    bool obstacle_detected_ = false;

    void imageCallback(const sensor_msgs::msg::Image::SharedPtr msg)
    {
        // Burada basit bir mantıkla engel olup olmadığını varsayıyoruz
        obstacle_detected_ = true; // Örnek olarak hep engel var gibi yapıyoruz.
    }
};
