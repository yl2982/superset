import {t} from '@superset-ui/translation';
import {ChartMetadata, ChartPlugin} from '@superset-ui/chart';
import transformProps from './transformProps';
import thumbnail from './images/thumbnail.png';

const metadata = new ChartMetadata({
    name: t('EChart Funnel'),
    description: '',
    thumbnail,
});

export default class FunnelPlugin extends ChartPlugin {
    constructor() {
        super({
            metadata,
            transformProps,
            loadChart: () => import('./Funnel.jsx'),
        });
    }
}
