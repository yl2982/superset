import {t} from '@superset-ui/translation';

export default {
    requiresTime: false,
    controlPanelSections: [
        {
            label: t('Query'),
            expanded: true,
            controlSetRows: [
                ['metrics'],
                ['adhoc_filters'],
                ['groupby'],
                ['limit'],
                ['row_limit', null],
            ],
        },
        {
            label: t('Chart Options'),
            controlSetRows: [
                ['color_scheme']
            ],
        },
    ],
};
