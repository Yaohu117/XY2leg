import os
from isaacgym import gymapi
from isaacgym import gymutil
"""
info:
======== Asset info xy2leg: ========
Got 17 bodies, 16 joints, and 16 DOFs
Bodies:
  0: 'base_link'
  1: 'Left_Link1'
  2: 'Left_Link2'
  3: 'Left_Link3'
  4: 'Left_Link4'
  5: 'Left_Link5'
  6: 'Left_Link6'
  7: 'Left_Wheel1'
  8: 'Left_Wheel2'
  9: 'Right_Link1'
 10: 'Right_Link2'
 11: 'Right_Link3'
 12: 'Right_Link4'
 13: 'Right_Link5'
 14: 'Right_Link6'
 15: 'Right_Wheel1'
 16: 'Right_Wheel2'
Joints:
  0: 'Left_Joint1' (Revolute)
  1: 'Left_Joint2' (Revolute)
  2: 'Left_Joint3' (Revolute)
  3: 'Left_Joint4' (Revolute)
  4: 'Left_Joint5' (Revolute)
  5: 'Left_Joint6' (Revolute)
  6: 'Left_Wheel1_Joint' (Revolute)
  7: 'Left_Wheel2_Joint' (Revolute)
  8: 'Right_Joint1' (Revolute)
  9: 'Right_Joint2' (Revolute)
 10: 'Right_Joint3' (Revolute)
 11: 'Right_Joint4' (Revolute)
 12: 'Right_Joint5' (Revolute)
 13: 'Right_Joint6' (Revolute)
 14: 'Right_Wheel1_Joint' (Revolute)
 15: 'Right_Wheel2_Joint' (Revolute)
DOFs:
  0: 'Left_Joint1' (Rotation)
  1: 'Left_Joint2' (Rotation)
  2: 'Left_Joint3' (Rotation)
  3: 'Left_Joint4' (Rotation)
  4: 'Left_Joint5' (Rotation)
  5: 'Left_Joint6' (Rotation)
  6: 'Left_Wheel1_Joint' (Rotation)
  7: 'Left_Wheel2_Joint' (Rotation)
  8: 'Right_Joint1' (Rotation)
  9: 'Right_Joint2' (Rotation)
 10: 'Right_Joint3' (Rotation)
 11: 'Right_Joint4' (Rotation)
 12: 'Right_Joint5' (Rotation)
 13: 'Right_Joint6' (Rotation)
 14: 'Right_Wheel1_Joint' (Rotation)
 15: 'Right_Wheel2_Joint' (Rotation)
=== Environment info: ================================================
1 actors total

===== Actor: xy2leg =======================================

Bodies
['base_link', 'Left_Link1', 'Left_Link2', 'Left_Link3', 'Left_Link4', 'Left_Link5', 'Left_Link6', 'Left_Wheel1', 'Left_Wheel2', 'Right_Link1', 'Right_Link2', 'Right_Link3', 'Right_Link4', 'Right_Link5', 'Right_Link6', 'Right_Wheel1', 'Right_Wheel2']
{'Left_Link1': 1, 'Left_Link2': 2, 'Left_Link3': 3, 'Left_Link4': 4, 'Left_Link5': 5, 'Left_Link6': 6, 'Left_Wheel1': 7, 'Left_Wheel2': 8, 'Right_Link1': 9, 'Right_Link2': 10, 'Right_Link3': 11, 'Right_Link4': 12, 'Right_Link5': 13, 'Right_Link6': 14, 'Right_Wheel1': 15, 'Right_Wheel2': 16, 'base_link': 0}

Joints
['Left_Joint1', 'Left_Joint2', 'Left_Joint3', 'Left_Joint4', 'Left_Joint5', 'Left_Joint6', 'Left_Wheel1_Joint', 'Left_Wheel2_Joint', 'Right_Joint1', 'Right_Joint2', 'Right_Joint3', 'Right_Joint4', 'Right_Joint5', 'Right_Joint6', 'Right_Wheel1_Joint', 'Right_Wheel2_Joint']
{'Left_Joint1': 0, 'Left_Joint2': 1, 'Left_Joint3': 2, 'Left_Joint4': 3, 'Left_Joint5': 4, 'Left_Joint6': 5, 'Left_Wheel1_Joint': 6, 'Left_Wheel2_Joint': 7, 'Right_Joint1': 8, 'Right_Joint2': 9, 'Right_Joint3': 10, 'Right_Joint4': 11, 'Right_Joint5': 12, 'Right_Joint6': 13, 'Right_Wheel1_Joint': 14, 'Right_Wheel2_Joint': 15}

 Degrees Of Freedom (DOFs)
['Left_Joint1', 'Left_Joint2', 'Left_Joint3', 'Left_Joint4', 'Left_Joint5', 'Left_Joint6', 'Left_Wheel1_Joint', 'Left_Wheel2_Joint', 'Right_Joint1', 'Right_Joint2', 'Right_Joint3', 'Right_Joint4', 'Right_Joint5', 'Right_Joint6', 'Right_Wheel1_Joint', 'Right_Wheel2_Joint']
{'Left_Joint1': 0, 'Left_Joint2': 1, 'Left_Joint3': 2, 'Left_Joint4': 3, 'Left_Joint5': 4, 'Left_Joint6': 5, 'Left_Wheel1_Joint': 6, 'Left_Wheel2_Joint': 7, 'Right_Joint1': 8, 'Right_Joint2': 9, 'Right_Joint3': 10, 'Right_Joint4': 11, 'Right_Joint5': 12, 'Right_Joint6': 13, 'Right_Wheel1_Joint': 14, 'Right_Wheel2_Joint': 15}

Poses from Body State:
[((-9.3132257e-10,  7.4505806e-09, 2.       ), (-0.7071068 , -2.3869795e-14, -1.2586807e-13,  0.7071068 ))
 (( 1.2600142e-01,  5.7714414e-02, 2.       ), ( 0.6532816 ,  2.7059808e-01,  2.7059814e-01,  0.6532815 ))
 (( 1.8525700e-01,  5.8916509e-02, 2.       ), ( 0.27059814, -6.5328157e-01,  2.7059799e-01,  0.6532815 ))
 (( 2.6158917e-01, -1.7886385e-03, 2.       ), (-0.27059796, -6.5328145e-01, -2.7059799e-01,  0.6532815 ))
 (( 2.9623741e-01, -2.5123153e-02, 2.       ), ( 0.27059808, -6.5328151e-01, -2.7059811e-01, -0.65328145))
 (( 3.9339390e-01, -1.2086542e-01, 2.       ), (-0.270598  , -6.5328151e-01,  2.7059802e-01, -0.65328145))
 (( 4.3115339e-01, -1.3401760e-01, 2.0000002), (-0.27059796,  6.5328431e-01, -2.7059588e-01, -0.6532796 ))
 (( 4.7782227e-01, -1.4745291e-01, 2.0225003), (-0.27059796,  6.5328431e-01, -2.7059588e-01, -0.6532796 ))
 (( 4.7782248e-01, -1.4745267e-01, 1.9775003), (-0.27059796,  6.5328431e-01, -2.7059588e-01, -0.6532796 ))
 ((-1.5328801e-01,  5.7714403e-02, 2.       ), ( 0.6532816 , -2.7059802e-01, -2.7059802e-01,  0.65328157))
 ((-2.1236680e-01,  5.8739685e-02, 2.       ), ( 0.6532814 ,  2.7059811e-01, -2.7059808e-01, -0.65328145))
 ((-2.8887576e-01, -1.7886795e-03, 2.       ), (-0.2705983 ,  6.5328157e-01, -2.7059808e-01, -0.65328145))
 ((-3.2352400e-01, -2.5123201e-02, 2.       ), (-0.27059814, -6.5328163e-01,  2.7059790e-01, -0.6532815 ))
 ((-4.2068046e-01, -1.2086550e-01, 2.0000002), (-0.6532816 ,  2.7059790e-01,  2.7059805e-01, -0.65328145))
 ((-4.5843998e-01, -1.3401771e-01, 2.0000002), ( 0.66931474,  2.7723834e-01, -2.6379123e-01, -0.63684446))
 ((-5.0429803e-01, -1.4826387e-01, 1.9763604), ( 0.66931415, -2.7723992e-01, -6.3684565e-01, -0.26378846))
 ((-5.0587893e-01, -1.4668274e-01, 2.0213048), ( 0.66931415, -2.7723992e-01, -6.3684565e-01, -0.26378846))]

Velocities from Body State:
[((0., 0., 0.), (0., 0., 0.)) ((0., 0., 0.), (0., 0., 0.))
 ((0., 0., 0.), (0., 0., 0.)) ((0., 0., 0.), (0., 0., 0.))
 ((0., 0., 0.), (0., 0., 0.)) ((0., 0., 0.), (0., 0., 0.))
 ((0., 0., 0.), (0., 0., 0.)) ((0., 0., 0.), (0., 0., 0.))
 ((0., 0., 0.), (0., 0., 0.)) ((0., 0., 0.), (0., 0., 0.))
 ((0., 0., 0.), (0., 0., 0.)) ((0., 0., 0.), (0., 0., 0.))
 ((0., 0., 0.), (0., 0., 0.)) ((0., 0., 0.), (0., 0., 0.))
 ((0., 0., 0.), (0., 0., 0.)) ((0., 0., 0.), (0., 0., 0.))
 ((0., 0., 0.), (0., 0., 0.))]

Body 'base_link' has position (-9.313226e-10, 7.450581e-09, 2.)
Body 'Left_Link1' has position (0.12600142, 0.05771441, 2.)
Body 'Left_Link2' has position (0.185257, 0.05891651, 2.)
Body 'Left_Link3' has position (0.26158917, -0.00178864, 2.)
Body 'Left_Link4' has position (0.2962374, -0.02512315, 2.)
Body 'Left_Link5' has position (0.3933939, -0.12086542, 2.)
Body 'Left_Link6' has position (0.4311534, -0.1340176, 2.0000002)
Body 'Left_Wheel1' has position (0.47782227, -0.1474529, 2.0225003)
Body 'Left_Wheel2' has position (0.47782248, -0.14745267, 1.9775003)
Body 'Right_Link1' has position (-0.153288, 0.0577144, 2.)
Body 'Right_Link2' has position (-0.2123668, 0.05873968, 2.)
Body 'Right_Link3' has position (-0.28887576, -0.00178868, 2.)
Body 'Right_Link4' has position (-0.323524, -0.0251232, 2.)
Body 'Right_Link5' has position (-0.42068046, -0.1208655, 2.0000002)
Body 'Right_Link6' has position (-0.45843998, -0.1340177, 2.0000002)
Body 'Right_Wheel1' has position (-0.50429803, -0.14826387, 1.9763604)
Body 'Right_Wheel2' has position (-0.5058789, -0.14668274, 2.0213048)

DOF states:
[(0., 0.) (0., 0.) (0., 0.) (0., 0.) (0., 0.) (0., 0.) (0., 0.) (0., 0.)
 (0., 0.) (0., 0.) (0., 0.) (0., 0.) (0., 0.) (0., 0.) (0., 0.) (0., 0.)]

DOF 'Left_Joint1' has position 0.0
DOF 'Left_Joint2' has position 0.0
DOF 'Left_Joint3' has position 0.0
DOF 'Left_Joint4' has position 0.0
DOF 'Left_Joint5' has position 0.0
DOF 'Left_Joint6' has position 0.0
DOF 'Left_Wheel1_Joint' has position 0.0
DOF 'Left_Wheel2_Joint' has position 0.0
DOF 'Right_Joint1' has position 0.0
DOF 'Right_Joint2' has position 0.0
DOF 'Right_Joint3' has position 0.0
DOF 'Right_Joint4' has position 0.0
DOF 'Right_Joint5' has position 0.0
DOF 'Right_Joint6' has position 0.0
DOF 'Right_Wheel1_Joint' has position 0.0
DOF 'Right_Wheel2_Joint' has position 0.0
"""

def print_asset_info(asset, name):
    print("======== Asset info %s: ========" % (name))
    num_bodies = gym.get_asset_rigid_body_count(asset)
    num_joints = gym.get_asset_joint_count(asset)
    num_dofs = gym.get_asset_dof_count(asset)
    print("Got %d bodies, %d joints, and %d DOFs" %
          (num_bodies, num_joints, num_dofs))

    # Iterate through bodies
    print("Bodies:")
    for i in range(num_bodies):
        name = gym.get_asset_rigid_body_name(asset, i)
        print(" %2d: '%s'" % (i, name))

    # Iterate through joints
    print("Joints:")
    for i in range(num_joints):
        name = gym.get_asset_joint_name(asset, i)
        type = gym.get_asset_joint_type(asset, i)
        type_name = gym.get_joint_type_string(type)
        print(" %2d: '%s' (%s)" % (i, name, type_name))

    # iterate through degrees of freedom (DOFs)
    print("DOFs:")
    for i in range(num_dofs):
        name = gym.get_asset_dof_name(asset, i)
        type = gym.get_asset_dof_type(asset, i)
        type_name = gym.get_dof_type_string(type)
        print(" %2d: '%s' (%s)" % (i, name, type_name))


def print_actor_info(gym, env, actor_handle):

    name = gym.get_actor_name(env, actor_handle)

    body_names = gym.get_actor_rigid_body_names(env, actor_handle)
    body_dict = gym.get_actor_rigid_body_dict(env, actor_handle)

    joint_names = gym.get_actor_joint_names(env, actor_handle)
    joint_dict = gym.get_actor_joint_dict(env, actor_handle)

    dof_names = gym.get_actor_dof_names(env, actor_handle)
    dof_dict = gym.get_actor_dof_dict(env, actor_handle)

    print()
    print("===== Actor: %s =======================================" % name)

    print("\nBodies")
    print(body_names)
    print(body_dict)

    print("\nJoints")
    print(joint_names)
    print(joint_dict)

    print("\n Degrees Of Freedom (DOFs)")
    print(dof_names)
    print(dof_dict)
    print()

    # Get body state information
    body_states = gym.get_actor_rigid_body_states(
        env, actor_handle, gymapi.STATE_ALL)

    # Print some state slices
    print("Poses from Body State:")
    print(body_states['pose'])          # print just the poses

    print("\nVelocities from Body State:")
    print(body_states['vel'])          # print just the velocities
    print()

    # iterate through bodies and print name and position
    body_positions = body_states['pose']['p']
    for i in range(len(body_names)):
        print("Body '%s' has position" % body_names[i], body_positions[i])

    print("\nDOF states:")

    # get DOF states
    dof_states = gym.get_actor_dof_states(env, actor_handle, gymapi.STATE_ALL)

    # print some state slices
    # Print all states for each degree of freedom
    print(dof_states)
    print()

    # iterate through DOFs and print name and position
    dof_positions = dof_states['pos']
    for i in range(len(dof_names)):
        print("DOF '%s' has position" % dof_names[i], dof_positions[i])

if __name__ == "__main__":
    # initialize gym
    gym = gymapi.acquire_gym()

    # parse arguments
    args = gymutil.parse_arguments(description="Asset and Environment Information")

    # create simulation context
    sim_params = gymapi.SimParams()

    sim_params.use_gpu_pipeline = False
    if args.use_gpu_pipeline:
        print("WARNING: Forcing CPU pipeline.")

    sim = gym.create_sim(args.compute_device_id, args.graphics_device_id, args.physics_engine, sim_params)

    if sim is None:
        print("*** Failed to create sim")
        quit()

    # Print out the working directory
    # helpful in determining the relative location that assets will be loaded from
    print("Working directory: %s" % os.getcwd())

    # load asserts
    asset_root = "/home/oy/DRL/isaacgym/unitree_rl_gym/resources/robots/twolegwheel"
    asset = "urdf/twolegwheel.urdf"
    asset_name = "xy2leg"
    print("Loading asset '%s' from '%s'" % (asset, asset_root))

    current_asset = gym.load_asset(sim, asset_root, asset)
    if current_asset is None:
        print("*** Failed to load asset '%s'" % (asset, asset_root))
        quit()

    print()
    print_asset_info(current_asset, asset_name)

    # Setup environment spacing
    spacing = 2.0
    lower = gymapi.Vec3(-spacing, 0.0, -spacing)
    upper = gymapi.Vec3(spacing, spacing, spacing)

    # Create one environment
    env = gym.create_env(sim, lower, upper, 1)

    # Add actors to environment
    pose = gymapi.Transform()

    pose.p = gymapi.Vec3(0.0, 0.0, 2)
    pose.r = gymapi.Quat(-0.707107, 0.0, 0.0, 0.707107)
    gym.create_actor(env, current_asset, pose, asset_name, -1, -1)

    print("=== Environment info: ================================================")

    actor_count = gym.get_actor_count(env)
    print("%d actors total" % actor_count)

    # Iterate through all actors for the environment
    for i in range(actor_count):
        actor_handle = gym.get_actor_handle(env, i)
        print_actor_info(gym, env, actor_handle)

    # Cleanup the simulator
    gym.destroy_sim(sim)
