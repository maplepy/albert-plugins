"""
Minimal ProtonDB Plugin Test for Albert

This is a simplified version to test the basic plugin structure and initialization.
"""

# Mandatory metadata
md_iid = "3.0"
md_version = "1.0"
md_name = "ProtonDB Test"
md_description = "Minimal ProtonDB test plugin"

# Optional metadata
md_license = "MIT"
md_url = "https://github.com/maplepy/albert-protondb"
md_authors = ["maplepy"]
md_bin_dependencies = []
md_lib_dependencies = []

import albert

class Plugin(albert.PluginInstance, albert.TriggerQueryHandler):

    def __init__(self):
        # Explicit initialization of both parent classes
        albert.PluginInstance.__init__(self)
        albert.TriggerQueryHandler.__init__(self)
        
        print("ProtonDB Test Plugin initialized successfully!")

    def defaultTrigger(self) -> str:
        return "ptest "

    def synopsis(self, query: str) -> str:
        return "ProtonDB Test: ptest <message>"

    def supportsFuzzyMatching(self) -> bool:
        return False

    def handleTriggerQuery(self, query: albert.Query):
        search_term = query.string.strip()

        if not search_term:
            query.add(albert.StandardItem(
                id="ptest_help",
                text="ProtonDB Test Plugin",
                subtext="Enter any text to test the plugin",
                iconUrls=["xdg:applications-games"],
                actions=[]
            ))
            return

        # Simple test response
        query.add(albert.StandardItem(
            id="ptest_response",
            text=f"Test: {search_term}",
            subtext="This is a test response from the ProtonDB test plugin",
            iconUrls=["xdg:dialog-information"],
            actions=[
                albert.Action(
                    "copy",
                    "Copy text",
                    lambda: albert.setClipboardText(search_term)
                )
            ]
        ))

    def finalize(self):
        """Clean up when plugin is disabled"""
        print("ProtonDB Test Plugin finalized")