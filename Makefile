.PHONY: validate system-info

validate:
	python3 scripts/validate_curriculum.py

system-info:
	python3 scripts/collect_system_info.py

