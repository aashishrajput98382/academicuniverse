import express from 'express';
import { authenticateUser, enforceOrgIsolation } from '../middleware/auth';
import {
  getGrowthAnalysis,
  getDomainPatterns,
  getPragmaticRemediation,
} from '../controllers/growthEngineController';

const router = express.Router();

router.use(authenticateUser, enforceOrgIsolation);

router.get('/analysis', getGrowthAnalysis);
router.get('/patterns', getDomainPatterns);
router.get('/remediation', getPragmaticRemediation);

export default router;
