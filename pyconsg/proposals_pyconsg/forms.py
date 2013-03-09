from django import forms
from django.utils.translation import ugettext_lazy as _

from markitup.widgets import MarkItUpWidget

from proposals_pyconsg.models import (
    TalkProposal,
    TutorialProposal,
    StartupBoothProposal,
)


class ProposalForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProposalForm, self).__init__(*args, **kwargs)
        self.fields['additional_notes'].label = _(
            'Notes to reviewers')

    def clean_description(self):
        value = self.cleaned_data["description"]
        if len(value) > 400:
            raise forms.ValidationError(
                u"The description must be less than 400 characters"
            )
        return value


class TalkProposalForm(ProposalForm):

    class Meta:
        model = TalkProposal
        fields = [
            "title",
            "audience_level",
            "description",
            "abstract",
            "additional_notes",
            "recording_release",
        ]
        widgets = {
            "abstract": MarkItUpWidget(),
            "additional_notes": MarkItUpWidget(),
        }


class TutorialProposalForm(ProposalForm):

    class Meta:
        model = TutorialProposal
        fields = [
            "title",
            "audience_level",
            "description",
            "abstract",
            "additional_notes",
            "recording_release",

        ]
        widgets = {
            "abstract": MarkItUpWidget(),
            "additional_notes": MarkItUpWidget(),
        }


class StartupBoothProposalForm(ProposalForm):

    class Meta:
        model = StartupBoothProposal
        fields = [
            "title",
            "audience_level",
            "description",
            "abstract",
            "additional_notes",
            "recording_release",

        ]
        widgets = {
            "abstract": MarkItUpWidget(),
            "additional_notes": MarkItUpWidget(),
        }
