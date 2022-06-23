import libhousy

first = True
def main(robot: libhousy.robot):
    if first:
        robot.rDriveEncoder.Reset()
        robot.lDriveEncoder.Reset()
        first=False

        robot.rDrive.Set(0.8)
        robot.lDrive.Set(0.8)

    if robot.rDriveEncoder.Get() > 120:
        robot.rDrive.Set(0)

    if robot.lDriveEncoder.Get() >120:
        robot.lDrive.Set(0)

    robot.rDriveEncoder.Get()


    robot.lDriveEncoder.Get()

    
    return libhousy.DONE
