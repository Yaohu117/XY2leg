from legged_gym.envs.base.legged_robot_config import LeggedRobotCfg, LeggedRobotCfgPPO

import numpy as np

class XY2LegCfg( LeggedRobotCfg ):
    class init_state( LeggedRobotCfg.init_state ):
        pos = [0.0, 0.0, 0.42] # x,y,z [m]
        default_joint_angles = { # = target angles [rad] when action = 0.0
            'Left_Joint1' : 90*np.pi/180,
            'Left_Joint2' : 40*np.pi/180,
            'Left_Joint3' : 80*np.pi/180,
            'Left_Joint4' : 0.,
            'Left_Joint5' : 0.,
            'Left_Joint6' : 0.,
            'Right_Joint1' : -90*np.pi/180,
            'Right_Joint2' : 40*np.pi/180,
            'Right_Joint3' : 80*np.pi/180,
            'Right_Joint4' : 0.,
            'Right_Joint5' : 0.,
            'Right_Joint6' : 0.,
        }
    
    class env(LeggedRobotCfg.env):
        num_observations = 47
        num_privileged_obs = 50
        num_actions = 12

    
    class domain_rand(LeggedRobotCfg.domain_rand):
        """ 域随机化：提高策略在真实世界的泛化能力 """
        randomize_friction = True
        friction_range = [0.1, 1.25]
        randomize_base_mass = True
        added_mass_range = [-1., 3.]
        push_robots = True
        push_interval_s = 5
        max_push_vel_xy = 1.5
      

    class control( LeggedRobotCfg.control ):
        # PD Drive parameters:
        control_type = 'P'
          # PD Drive parameters:
        stiffness = {
                    'Left_Joint1' : 100,
                    'Left_Joint2' : 100,
                    'Left_Joint3' : 100,
                    'Left_Joint4' : 150,
                    'Left_Joint5' : 40,
                    'Left_Joint6' : 40,
                    'Right_Joint1' : 100,
                    'Right_Joint2' : 100,
                    'Right_Joint3' : 100,
                    'Right_Joint4' : 150,
                    'Right_Joint5' : 40,
                    'Right_Joint6' : 40,
                     }  # [N*m/rad]
        damping = {
                    'Left_Joint1' : 2,
                    'Left_Joint2' : 2,
                    'Left_Joint3' : 2,
                    'Left_Joint4' : 4,
                    'Left_Joint5' : 2,
                    'Left_Joint6' : 2,
                    'Right_Joint1' : 2,
                    'Right_Joint2' : 2,
                    'Right_Joint3' : 2,
                    'Right_Joint4' : 4,
                    'Right_Joint5' : 2,
                    'Right_Joint6' : 2,
                     }  # [N*m/rad]  # [N*m*s/rad]
        # action scale: target angle = actionScale * action + defaultAngle
        action_scale = 0.25
        # decimation: Number of control action updates @ sim DT per policy DT
        decimation = 4

    class asset( LeggedRobotCfg.asset ):
        file = '{LEGGED_GYM_ROOT_DIR}/resources/robots/twolegwheel/urdf/twolegwheel.urdf'
        name = "xy2leg"
        foot_name = "Link6" # 地面接触判断
        penalize_contacts_on = ["Link1", "Link2", "Link3", "Link4", "Link5"] # 接触地面给惩罚的杆件
        terminate_after_contacts_on = ["base_link"] # 接触地面给终止的杆件
        self_collisions = 0 # 1 to disable, 0 to enable...bitwise filter
        flip_visual_attachments = False
  
    class rewards( LeggedRobotCfg.rewards ):
        soft_dof_pos_limit = 0.9
        base_height_target = 0.42 # 预估
        
        class scales( LeggedRobotCfg.rewards.scales ):
            tracking_lin_vel = 1.0
            tracking_ang_vel = 0.5
            lin_vel_z = 0 #-2.0
            ang_vel_xy = -0.05
            orientation = -1.0
            base_height = -10.0
            dof_acc = 0 # -2.5e-7
            dof_vel = 0 # -1e-3
            feet_air_time = 0.0
            collision = 0.0
            action_rate = -0.01
            dof_pos_limits = -5.0
            alive = 0.15
            # hip_pos = 0.0 # -1.0
            contact_no_vel = -0.2
            feet_swing_height = -20.0
            contact = 0.18

class XY2LegCfgPPO( LeggedRobotCfgPPO ):
    class policy:
        init_noise_std = 0.8
        actor_hidden_dims = [32]
        critic_hidden_dims = [32]
        activation = 'elu' # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid
        # only for 'ActorCriticRecurrent':
        rnn_type = 'lstm'
        rnn_hidden_size = 64
        rnn_num_layers = 1
        
    class algorithm( LeggedRobotCfgPPO.algorithm ):
        entropy_coef = 0.01
    class runner( LeggedRobotCfgPPO.runner ):
        policy_class_name = "ActorCriticRecurrent"
        max_iterations = 10000
        run_name = ''
        experiment_name = 'xy2leg'

    