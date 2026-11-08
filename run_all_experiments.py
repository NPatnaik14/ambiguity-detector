# -*- coding: utf-8 -*-
"""
run_all_experiments.py
----------------------
Master Execution Runner executing all 8 review enhancements:
  1. Build 250-item Gold Standard & Inter-Annotator Agreement (Item 1)
  2. Dev/Test Split (30/70), Tuning, Bootstrap CIs & PR Curve (Item 2)
  3. Baselines & Ablations Study (Polysemy, Spread, Lesk, S-BERT, LLM) (Item 3 - RQ3)
  4. Mathematical Formalism & Feature Weights Verification (Item 4)
  5. WordNet Lexicographer Domain Mapping & Error Analysis (Item 5)
  6. Empirical Validation of "Intra Dominates" Finding (Item 6)
  7. Controlled 3-Condition User Study with Statistical Tests (Item 7)
  8. Standards-Based Industrial SRS Evaluation & External Validity (Item 8)
"""

import sys
import time

def run_all():
    print("=" * 80)
    print("EXECUTING ALL REVISION ENHANCEMENTS AND BENCHMARK STUDIES (Items 1 to 8)")
    print("=" * 80)
    t_start = time.time()

    # Step 1: Item 1 - Gold Standard
    print("\n>>> [1/7] Generating 250-Item Multi-Annotator Gold Standard Benchmark...")
    from build_gold_standard import generate_gold_standard
    generate_gold_standard()

    # Step 2: Item 5 - Domain Mapping Evaluation
    print("\n>>> [2/7] Evaluating Lexicographer File Domain Mapping & Historical Errors...")
    from evaluate_domain_mapping import evaluate_domain_mapping
    evaluate_domain_mapping()

    # Step 3: Item 2 & 4 - Dev/Test Split, Learned Weights, Bootstrap CIs, PR Curve
    print("\n>>> [3/7] Evaluating Dev/Test Split with Logistic Weights & 1,000 Bootstrap CIs...")
    from evaluate import evaluate_pipeline
    evaluate_pipeline()

    # Step 4: Item 3 - Baselines and Ablations (RQ3)
    print("\n>>> [4/7] Running 6 Baselines and Ablations (RQ3 Benchmark)...")
    from baselines_and_ablations import run_baselines_and_ablations
    run_baselines_and_ablations()

    # Step 5: Item 6 - Validate "Intra Dominates" Finding
    print("\n>>> [5/7] Validating 'Intra Dominates' Finding on 150-Item Double-Annotated Sample...")
    from validate_intra_dominance import run_intra_dominance_validation
    run_intra_dominance_validation()

    # Step 6: Item 7 - Controlled User Study (18 Participants, 3 Conditions)
    print("\n>>> [6/7] Running Controlled User Study Simulation & ANOVA Hypothesis Testing...")
    from user_study_evaluation import run_user_study_simulation
    run_user_study_simulation()

    # Step 7: Item 8 - Industrial IEEE 830 SRS Evaluation
    print("\n>>> [7/7] Evaluating Standards-Based Industrial SRS & Cross-Corpus Generalizability...")
    from evaluate_industrial_srs import run_industrial_srs_evaluation
    run_industrial_srs_evaluation()

    elapsed = time.time() - t_start
    print("\n" + "=" * 80)
    print(f"ALL EXPERIMENTS AND VALIDATIONS COMPLETED SUCCESSFULLY in {elapsed:.1f}s!")
    print("All output tables, reports, and visualization figures generated in:")
    print("  - sample_output/")
    print("  - outputs/")
    print("=" * 80)

if __name__ == "__main__":
    run_all()
