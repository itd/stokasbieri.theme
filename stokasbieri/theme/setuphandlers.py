def setupVarious(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if context.readDataFile('stokasbieri.theme_various.txt') is None:
        return

    # Hide some actions
    #actionsTool = self.portal_actions
    #act = actionsTool.getActionInfo("portal_tabs/index_html")
    #act.condition = "python: False"

    # Add additional setup code here
