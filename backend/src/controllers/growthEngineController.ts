import { Request, Response } from 'express';
import { StudentGrowthEngineService } from '../services/studentGrowthEngine.service';
import { sendResponse, sendError } from '../utils/response';

const growthEngineService = new StudentGrowthEngineService();

export const getGrowthAnalysis = async (req: Request, res: Response) => {
  try {
    const authUserId = (req as any).user?.userId;
    const organizationId = (req as any).organizationId || (req as any).user?.organizationId;

    if (!authUserId) {
      return sendError(res, 401, 'Authentication required');
    }

    const report = await growthEngineService.analyzeStudentGrowth(authUserId, organizationId);
    return sendResponse(res, 200, report, 'Student growth intelligence analysis retrieved successfully');
  } catch (error: any) {
    console.error('GrowthEngine getGrowthAnalysis error:', error);
    return sendError(res, 500, error.message || 'Failed to analyze student growth');
  }
};

export const getDomainPatterns = async (req: Request, res: Response) => {
  try {
    const authUserId = (req as any).user?.userId;
    const organizationId = (req as any).organizationId || (req as any).user?.organizationId;

    if (!authUserId) {
      return sendError(res, 401, 'Authentication required');
    }

    const report = await growthEngineService.analyzeStudentGrowth(authUserId, organizationId);
    return sendResponse(res, 200, report.domainAffinity, 'Domain affinity and patterns retrieved successfully');
  } catch (error: any) {
    console.error('GrowthEngine getDomainPatterns error:', error);
    return sendError(res, 500, error.message || 'Failed to retrieve domain patterns');
  }
};

export const getPragmaticRemediation = async (req: Request, res: Response) => {
  try {
    const authUserId = (req as any).user?.userId;
    const organizationId = (req as any).organizationId || (req as any).user?.organizationId;

    if (!authUserId) {
      return sendError(res, 401, 'Authentication required');
    }

    const report = await growthEngineService.analyzeStudentGrowth(authUserId, organizationId);
    return sendResponse(res, 200, report.remediation, 'Pragmatic industry remediation advice retrieved successfully');
  } catch (error: any) {
    console.error('GrowthEngine getPragmaticRemediation error:', error);
    return sendError(res, 500, error.message || 'Failed to retrieve remediation advice');
  }
};
