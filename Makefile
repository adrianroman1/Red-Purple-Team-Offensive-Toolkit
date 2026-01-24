.PHONY: run cert clean

run:
	python run_validation.py

cert:
	python -c "from core_validation.zero_knowledge_proof import ZeroKnowledgeProofGenerator; print(ZeroKnowledgeProofGenerator().create_certificate())"

clean:
	rm -rf data/vault/*.txt data/vault/*.html

