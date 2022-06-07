init -990 python in mas_submod_utils:
    Submod(
        author="MAS Self Harm Submod Team",
        name="MAS Self Harm Submod",
        description="Awareness about self-harm and support to self-harmers, with different "
                    "techniques, milestones, checkups and new dialogue and spritepacks.",
        version="1.0.4",
        dependencies={},
        settings_pane=None,
        version_updates={
            # Versions prior to 1.0.5 are affected
            "mas_self_harm_submod_team_mas_self_harm_submod_v1_0_0": "mas_self_harm_submod_team_mas_self_harm_submod_v1_0_5",
            "mas_self_harm_submod_team_mas_self_harm_submod_v1_0_1": "mas_self_harm_submod_team_mas_self_harm_submod_v1_0_5",
            "mas_self_harm_submod_team_mas_self_harm_submod_v1_0_2": "mas_self_harm_submod_team_mas_self_harm_submod_v1_0_5",
            "mas_self_harm_submod_team_mas_self_harm_submod_v1_0_3": "mas_self_harm_submod_team_mas_self_harm_submod_v1_0_5",
            "mas_self_harm_submod_team_mas_self_harm_submod_v1_0_4": "mas_self_harm_submod_team_mas_self_harm_submod_v1_0_5"
        }
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="MAS Self Harm Submod",
            user_name="my-otter-self",
            repository_name="mas_selfharm",
            submod_dir="/Submods/MAS Self Harm Submod",
            extraction_depth=3,
            redirected_files=(
                "README.md",
                "LICENSE.txt"
            )
        )
