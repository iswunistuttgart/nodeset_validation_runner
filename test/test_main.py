from unittest import TestCase

from main import get_job_id, prepare_input_data_from_config


class Test(TestCase):
    def test_get_job_id(self):
        expected_job_id = 1977
        test_text = """
        <li class="nav-item mr-2">
        <a href="/NodeSetValidator/Home/Results/1977">Results</a>
        </li>
        </ul>
        </nav>
        
        """
        job_id = get_job_id(test_text)
        self.assertEqual(str(job_id), str(expected_job_id))

    def test_prepare_input_data_from_config(self):
        expected_data = {
            "email": "max@mustermann.de",
            "ignoreTypes": "BaseObjectType",
            "suppressErrors": "InvalideNodeClass",
            "noDelete": "false",
            "checkConformanceUnits": "false"
        }
        config_path = "config.json"
        data, files = prepare_input_data_from_config(config_path)
        self.assertEqual(expected_data,data)
        self.assertEqual("nodesetFile", files[0][0])
        self.assertEqual("../assets/coffeemachine.nodeset2.xml", files[0][1].name)
        self.assertEqual("supportingNodeSetFiles", files[1][0])
        self.assertEqual("../assets/deps/Opc.Ua.Di.NodeSet2.xml", files[1][1].name)
        self.assertEqual("supportingNodeSetFiles", files[2][0])
        self.assertEqual("../assets/deps/Opc.Ua.Ia.NodeSet2.xml", files[2][1].name)
        self.assertEqual("supportingNodeSetFiles", files[3][0])
        self.assertEqual("../assets/deps/Opc.Ua.Machinery.NodeSet2.xml", files[3][1].name)
        self.assertEqual("specificationFile", files[4][0])
        self.assertEqual("../assets/example.docx", files[4][1].name)
