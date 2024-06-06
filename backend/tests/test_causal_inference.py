import pytest
from fastapi.testclient import TestClient
import pandas as pd

def test_estimate_effect(client: TestClient):
    model_spec = {
        "data": {
            "task_type": ["Feature", "Bugfix"],
            "loc": [50, 150],
            "files_touched": [1, 3],
            "author": ["Alice", "Bob"],
            "committer": ["Alice", "Bob"],
            "communication": [0.5, 0.8],
            "author_experience": [2, 5],
            "committer_experience": [3, 4],
            "contribution_complexity": [0.7, 1.2],
            "avg_token": [20, 35],
            "total_nloc": [200, 300],
            "avg_ccn": [1.1, 2.0],
            "has_bug_fixing": [True, False],
            "has_code_refactoring": [False, True]
        },
        "causal_graph": """
        digraph {
            task_type [label="Task Type"];
            loc [label="Lines of Code (LOC)"];
            files_touched [label="Number of Files Touched"];
            author [label="Author"];
            committer [label="Committer"];
            communication [label="Communication"];
            author_experience [label="Author Experience"];
            committer_experience [label="Committer Experience"];
            contribution_complexity [label="Contribution Complexity"];
            avg_token [label="Avg. token count of functions."];
            total_nloc [label="Total lines of code without comments"];
            avg_ccn [label="Avg. Cyclomatic Complexity Number"];
            has_bug_fixing [label="Has bug fixing?"];
            has_code_refactoring [label="Has code refactoring?"];
            U[label="Unobserved confounders"];
            U->communication;
            
            task_type -> has_bug_fixing;
            task_type -> has_code_refactoring;
            has_bug_fixing -> avg_ccn;
            has_bug_fixing -> contribution_complexity;
            has_code_refactoring -> avg_ccn;
            has_code_refactoring -> contribution_complexity;
            loc -> total_nloc;
            total_nloc -> avg_nloc;
            total_nloc -> contribution_complexity;
            total_nloc -> avg_token;
            files_touched -> contribution_complexity;
            files_touched -> avg_ccn;
            author -> avg_ccn;
            author -> contribution_complexity;
            author -> communication;
            committer -> avg_ccn;
            committer -> contribution_complexity;
            committer -> communication;
            author_experience -> avg_ccn;
            author_experience -> contribution_complexity;
            committer_experience -> avg_ccn;
            committer_experience -> contribution_complexity;
            communication -> contribution_complexity;
            communication -> avg_ccn;
            contribution_complexity -> avg_ccn;
        }
        """,
        "treatment": "communication",
        "outcome": "avg_ccn"
    }

    response = client.post("/causal_inference/effect_estimation/", json=model_spec)
    assert response.status_code == 200
    assert "Causal Estimate is" in response.json()["message"]
