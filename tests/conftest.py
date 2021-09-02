from userinput import UserInput
import pytest

user_input = UserInput()
user_input.deserialize("user_input.xml", user_input=True)
user_input.serialize("user_input_ser.xml")
user_input_ser = UserInput()
user_input_ser.deserialize("user_input_ser.xml")
user_input_ser.serialize("user_input_ser2.xml")
for k, v in user_input_ser.__dict__.items():
    print(k, v)

@pytest.fixture(scope="session")
def tmp_test_files_dir(
        tmpdir_factory
        ):
    test_files_tmpdir_factory = \
        tmpdir_factory.mktemp('test_files')
    yield test_files_tmpdir_factory
    shutil.rmtree(str(test_files_tmpdir_factory))



