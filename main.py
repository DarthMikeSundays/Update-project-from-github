import os
import sys


class MainSingleton(object):
    _instance = None
    BASE_DIRECTORY_FOR_CODING_STUFF = r"C:\\Users\ProMikeSundays\Documents\Coding Stuff"

    def __new__(cls, *args):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    # the main method
    def run(self):
        self.define_base_user_dependent_variables()
        self.process_operation_to_do()
        self.define_directory_to_use()
        self.confirm_directory_to_use()
        print(self.directory_to_use)
        os.chdir(self.directory_to_use)
        self.clone_github_project()
        self.operation_to_do == "UPDATE" and self.special_update_actions()

    def error(self, error_message):
        print(error_message)
        print("Exiting...")
        e   xit()

    # the input that is common to both operations
    def define_base_user_dependent_variables(self):
        self.github_project_name = input(
            "What's the name of the github project?")
        self.operation_to_do = (input(
            "Do you want to update a existing dir or just clone to create a new one? Type either update or create. ") or "update")

    def process_operation_to_do(self):
        OPERATIONS_CAN_DO = ["CREATE", "UPDATE"]

        self.operation_to_do = self.operation_to_do.upper()

        if self.operation_to_do not in OPERATIONS_CAN_DO:
            self.error(
                f"{self.operation_to_do} is an unknown operation")

    def define_directory_to_use(self):
        self.define_directory_to_use_by_user_input(
        ) if self.operation_to_do == "CREATE" else self.define_directory_to_use_by_finding_github_project_name()

    # used in the CREATE operation
    def define_directory_to_use_by_user_input(self):
        subdirectory_to_use = input(
            f"Inside {self.BASE_DIRECTORY_FOR_CODING_STUFF} where do you want to create the clone?")
        self.directory_to_use = os.path.join(
            self.BASE_DIRECTORY_FOR_CODING_STUFF, subdirectory_to_use)

    # used in the UPDATE operation
    def define_directory_to_use_by_finding_github_project_name(self):
        for root, directories, _ in os.walk(self.BASE_DIRECTORY_FOR_CODING_STUFF):

            if self.github_project_name in directories:
                self.directory_to_use = root
                break

        else:
            self.error(
                f"Inside {self.BASE_DIRECTORY_FOR_CODING_STUFF} no directory named {self.github_project_name} exists. Maybe you want to use the create command instead?")

    def confirm_directory_to_use(self):
        confirmed = input(
            f"Are you sure that you want to use the following directory: {self.directory_to_use} ? Type either yes or no ")

        if confirmed.upper() not in ["YES", "NO"]:
            self.error(f"{confirmed} is a unknown option:-(")

        message = f"Successfully {'confirmed' if confirmed=='yes' else 'cancelled'} operation: -)"

        if not confirmed:
            self.error(message)

        print(message)

    def clone_github_project(self):
        print("Cloning github repo...")
        self.temporary_cloned_dir_name = f"temporary{self.github_project_name}"
        command_to_clone = f"git clone https://github.com/ProMikeCoder2020/{self.github_project_name} {self.temporary_cloned_dir_name}"
        os.system(command_to_clone)

    def special_update_actions(self):
        self.old_directory_path = os.path.join(
            self.directory_to_use, self.github_project_name)
        self.new_directory_path = os.path.join(
            self.directory_to_use, self.temporary_cloned_dir_name)

        # an array of this format: Array<[action, conditionPath]>
        # the condition is the file or dir that must exist in the new_directory so
        # the special action can have any effect (this comment continues the prev. comment)
        SPECIAL_UPDATE_ACTIONS_AND_CONDITIONS = [
            [self.node_modules_action, "package.json"]]

        for [special_update_action, conditionPath] in SPECIAL_UPDATE_ACTIONS_AND_CONDITIONS:
            processedConditionPath = os.path.join(
                self.new_directory_path, conditionPath)
            print(processedConditionPath, os.path.exists(processedConditionPath))
            os.path.exists(processedConditionPath) and special_update_action

    def node_modules_action(self):


if __name__ == "__main__":
    mainInstance = MainSingleton()
    mainInstance.run()
