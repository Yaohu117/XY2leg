import os
from isaacgym import gymapi
from isaacgym import gymutil
"""
info:
======== Asset info g1: ========
Got 31 bodies, 30 joints, and 12 DOFs
Bodies:
  0: 'pelvis'
  1: 'imu_in_pelvis'
  2: 'left_hip_pitch_link'
  3: 'left_hip_roll_link'
  4: 'left_hip_yaw_link'
  5: 'left_knee_link'
  6: 'left_ankle_pitch_link'
  7: 'left_ankle_roll_link'
  8: 'pelvis_contour_link'
  9: 'right_hip_pitch_link'
 10: 'right_hip_roll_link'
 11: 'right_hip_yaw_link'
 12: 'right_knee_link'
 13: 'right_ankle_pitch_link'
 14: 'right_ankle_roll_link'
 15: 'torso_link'
 16: 'd435_link'
 17: 'head_link'
 18: 'imu_in_torso'
 19: 'left_shoulder_pitch_link'
 20: 'left_shoulder_roll_link'
 21: 'left_shoulder_yaw_link'
 22: 'left_elbow_link'
 23: 'left_wrist_roll_rubber_hand'
 24: 'logo_link'
 25: 'mid360_link'
 26: 'right_shoulder_pitch_link'
 27: 'right_shoulder_roll_link'
 28: 'right_shoulder_yaw_link'
 29: 'right_elbow_link'
 30: 'right_wrist_roll_rubber_hand'
Joints:
  0: 'imu_in_pelvis_joint' (Fixed)
  1: 'left_hip_pitch_joint' (Revolute)
  2: 'left_hip_roll_joint' (Revolute)
  3: 'left_hip_yaw_joint' (Revolute)
  4: 'left_knee_joint' (Revolute)
  5: 'left_ankle_pitch_joint' (Revolute)
  6: 'left_ankle_roll_joint' (Revolute)
  7: 'pelvis_contour_joint' (Fixed)
  8: 'right_hip_pitch_joint' (Revolute)
  9: 'right_hip_roll_joint' (Revolute)
 10: 'right_hip_yaw_joint' (Revolute)
 11: 'right_knee_joint' (Revolute)
 12: 'right_ankle_pitch_joint' (Revolute)
 13: 'right_ankle_roll_joint' (Revolute)
 14: 'waist_yaw_joint' (Fixed)
 15: 'd435_joint' (Fixed)
 16: 'head_joint' (Fixed)
 17: 'imu_in_torso_joint' (Fixed)
 18: 'left_shoulder_pitch_joint' (Fixed)
 19: 'left_shoulder_roll_joint' (Fixed)
 20: 'left_shoulder_yaw_joint' (Fixed)
 21: 'left_elbow_joint' (Fixed)
 22: 'left_wrist_roll_joint' (Fixed)
 23: 'logo_joint' (Fixed)
 24: 'mid360_joint' (Fixed)
 25: 'right_shoulder_pitch_joint' (Fixed)
 26: 'right_shoulder_roll_joint' (Fixed)
 27: 'right_shoulder_yaw_joint' (Fixed)
 28: 'right_elbow_joint' (Fixed)
 29: 'right_wrist_roll_joint' (Fixed)
DOFs:
  0: 'left_hip_pitch_joint' (Rotation)
  1: 'left_hip_roll_joint' (Rotation)
  2: 'left_hip_yaw_joint' (Rotation)
  3: 'left_knee_joint' (Rotation)
  4: 'left_ankle_pitch_joint' (Rotation)
  5: 'left_ankle_roll_joint' (Rotation)
  6: 'right_hip_pitch_joint' (Rotation)
  7: 'right_hip_roll_joint' (Rotation)
  8: 'right_hip_yaw_joint' (Rotation)
  9: 'right_knee_joint' (Rotation)
 10: 'right_ankle_pitch_joint' (Rotation)
 11: 'right_ankle_roll_joint' (Rotation)
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
    asset_root = "/home/oy/DRL/isaacgym/unitree_rl_gym/resources/robots/g1_description"
    asset = "g1_12dof.urdf"
    asset_name = "g1"
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
