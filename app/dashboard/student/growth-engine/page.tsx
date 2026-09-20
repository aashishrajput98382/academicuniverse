'use client';

import { useEffect, useState } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { useAuth } from '@/lib/AuthContext';
import { apiRequest } from '@/utils/api';
import {
  TrendingUp,
  TrendingDown,
  Minus,
  Sparkles,
  AlertTriangle,
  CheckCircle2,
  ShieldCheck,
  Brain,
  Code2,
  Cpu,
  Layers,
  BookOpen,
  ArrowRight,
  ExternalLink,
  Bot,
  Zap,
  RefreshCw,
  Compass,
  FileText,
  Flame,
} from 'lucide-react';

interface ISemesterSnapshot {
  semesterNumber: number;
  semesterName: string;
  sgpa: number;
  credits: number;
  attendancePercentage: number;
  subjectCount: number;
}

interface IDomainAffinity {
  cluster: string;
  displayName: string;
  averageScore: number;
  subjectCount: number;
  affinityIndex: number;
  status: 'STRENGTH' | 'BALANCED' | 'FRICTION_POINT';
}

interface IRemediationAdvice {
  subjectCode: string;
  subjectName: string;
  scoreOrGrade: string;
  numericScore: number;
  cluster: string;
  industryRelevanceScore: number;
  priority: 'CRITICAL_CORE' | 'FOUNDATIONAL' | 'PASS_ONLY_AUXILIARY';
  rootCause: string;
  rootCauseExplanation: string;
  pragmaticAdvice: string;
  industryContext: string;
}

interface IGrowthReport {
  studentId: string;
  studentName: string;
  trajectory: {
    direction: string;
    currentSgpa: number;
    previousSgpa: number;
    velocity: number;
    acceleration: number;
    momentumScore: number;
    overallCgpa: number;
    trajectoryDescription: string;
    attendanceGradeCovarianceAlert: boolean;
    covarianceMessage: string;
    semesterHistory: ISemesterSnapshot[];
  };
  domainAffinity: {
    archetype: string;
    archetypeDescription: string;
    primaryStrength: string;
    primaryFrictionPoint: string;
    clusterBreakdown: IDomainAffinity[];
  };
  remediation: {
    flaggedSubjectsCount: number;
    highRoiCount: number;
    passOnlyCount: number;
    actionPlan: IRemediationAdvice[];
  };
  chatbotContextSummary: {
    shortDirective: string;
    seniorMentorPromptSnippet: string;
  };
}

export default function StudentGrowthEnginePage() {
  const { user, backendToken } = useAuth();
  const router = useRouter();
  const [loading, setLoading] = useState<boolean>(true);
  const [report, setReport] = useState<IGrowthReport | null>(null);
  const [refreshing, setRefreshing] = useState<boolean>(false);

  const fetchGrowthReport = async () => {
    try {
      setLoading(true);
      const res: any = await apiRequest('/api/growth-engine/analysis', {
        headers: backendToken ? { Authorization: `Bearer ${backendToken}` } : {},
      });
      if (res?.data) {
        setReport(res.data);
      }
    } catch (err) {
      console.error('Failed to load growth engine report:', err);
    } finally {
      setLoading(false);
      setRefreshing(false);
    }
  };

  useEffect(() => {
    fetchGrowthReport();
  }, [backendToken]);

  const handleRefresh = () => {
    setRefreshing(true);
    fetchGrowthReport();
  };

  // Helper colors and icons for trajectory
  const getTrajectoryStyle = (direction: string = '') => {
    switch (direction) {
      case 'ACCELERATING_UPWARD':
        return {
          bg: 'from-emerald-950/50 via-teal-900/30 to-slate-900',
          border: 'border-emerald-500/40',
          badgeBg: 'bg-emerald-500/20 text-emerald-400 border-emerald-500/30',
          badgeText: 'Accelerating Upward',
          icon: <Sparkles className="w-5 h-5 text-emerald-400 animate-pulse" />,
        };
      case 'STEADY_GROWTH':
        return {
          bg: 'from-blue-950/50 via-cyan-900/30 to-slate-900',
          border: 'border-blue-500/40',
          badgeBg: 'bg-blue-500/20 text-blue-400 border-blue-500/30',
          badgeText: 'Steady Growth',
          icon: <TrendingUp className="w-5 h-5 text-blue-400" />,
        };
      case 'STABLE_PLATEAU':
        return {
          bg: 'from-amber-950/40 via-yellow-900/20 to-slate-900',
          border: 'border-amber-500/40',
          badgeBg: 'bg-amber-500/20 text-amber-400 border-amber-500/30',
          badgeText: 'Performance Plateau',
          icon: <Minus className="w-5 h-5 text-amber-400" />,
        };
      case 'CRITICAL_DROP':
        return {
          bg: 'from-rose-950/60 via-red-900/30 to-slate-900',
          border: 'border-rose-500/40',
          badgeBg: 'bg-rose-500/20 text-rose-400 border-rose-500/30',
          badgeText: 'Critical Academic Alert',
          icon: <AlertTriangle className="w-5 h-5 text-rose-400 animate-bounce" />,
        };
      default:
        return {
          bg: 'from-slate-900 via-indigo-950/30 to-slate-900',
          border: 'border-indigo-500/40',
          badgeBg: 'bg-indigo-500/20 text-indigo-400 border-indigo-500/30',
          badgeText: 'Moderate Transition',
          icon: <TrendingDown className="w-5 h-5 text-indigo-400" />,
        };
    }
  };

  const getClusterIcon = (cluster: string) => {
    switch (cluster) {
      case 'core_cs_systems':
        return <Code2 className="w-5 h-5 text-blue-400" />;
      case 'applied_dev_cloud':
        return <Zap className="w-5 h-5 text-emerald-400" />;
      case 'theoretical_math':
        return <Brain className="w-5 h-5 text-purple-400" />;
      case 'hardware_electronics':
        return <Cpu className="w-5 h-5 text-amber-400" />;
      default:
        return <BookOpen className="w-5 h-5 text-slate-400" />;
    }
  };

  if (loading && !report) {
    return (
      <div className="flex flex-col items-center justify-center min-h-[60vh] space-y-4">
        <div className="w-12 h-12 border-4 border-indigo-500/30 border-t-indigo-500 rounded-full animate-spin" />
        <p className="text-slate-400 text-sm font-medium">Analyzing multi-semester growth patterns...</p>
      </div>
    );
  }

  const trajStyle = getTrajectoryStyle(report?.trajectory?.direction);
  const criticalRemediations = report?.remediation?.actionPlan?.filter((a) => a.priority === 'CRITICAL_CORE') || [];
  const passOnlyRemediations = report?.remediation?.actionPlan?.filter((a) => a.priority === 'PASS_ONLY_AUXILIARY') || [];
  const foundationalRemediations = report?.remediation?.actionPlan?.filter((a) => a.priority === 'FOUNDATIONAL') || [];

  return (
    <div className="space-y-8 max-w-7xl mx-auto pb-12">
      {/* Top Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-slate-800/80 pb-6">
        <div>
          <div className="flex items-center gap-2 mb-1">
            <span className="px-2.5 py-0.5 text-[11px] font-bold tracking-wider uppercase rounded-full bg-indigo-500/10 text-indigo-400 border border-indigo-500/20">
              Part 2 • Core Engine
            </span>
            <span className="text-slate-400 text-xs">• Longitudinal Pattern Mining</span>
          </div>
          <h1 className="text-2xl md:text-3xl font-extrabold text-white tracking-tight flex items-center gap-2.5">
            Student Growth Intelligence Engine
            <Sparkles className="w-6 h-6 text-amber-400" />
          </h1>
          <p className="text-slate-400 text-sm mt-1 max-w-3xl">
            Semester-over-semester momentum analytics, cognitive domain affinity detection, and pragmatic industry-aligned remediation.
          </p>
        </div>

        <div className="flex items-center gap-3">
          <button
            onClick={handleRefresh}
            disabled={refreshing}
            className="flex items-center gap-2 px-3.5 py-2 text-xs font-medium text-slate-300 bg-slate-900/80 hover:bg-slate-800 border border-slate-700/60 rounded-xl transition-all shadow-sm disabled:opacity-50"
          >
            <RefreshCw className={`w-3.5 h-3.5 ${refreshing ? 'animate-spin' : ''}`} />
            Sync Growth
          </button>
          <Link
            href="/dashboard/student/chatbot"
            className="flex items-center gap-2 px-4 py-2 text-xs font-semibold text-white bg-gradient-to-r from-indigo-600 to-blue-600 hover:from-indigo-500 hover:to-blue-500 rounded-xl transition-all shadow-lg shadow-indigo-500/20"
          >
            <Bot className="w-4 h-4" />
            Talk to AI Mentor
          </Link>
        </div>
      </div>

      {/* Trajectory Momentum Hero Banner */}
      <div
        className={`relative overflow-hidden rounded-2xl border ${trajStyle.border} bg-gradient-to-br ${trajStyle.bg} p-6 md:p-8 backdrop-blur-xl shadow-2xl transition-all`}
      >
        <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-6">
          <div className="space-y-3 max-w-2xl">
            <div className="flex items-center gap-3">
              <span className={`inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold border ${trajStyle.badgeBg}`}>
                {trajStyle.icon}
                {trajStyle.badgeText}
              </span>
              <span className="text-xs text-slate-400 font-medium">
                Velocity: {report?.trajectory?.velocity ? (report.trajectory.velocity > 0 ? `+${report.trajectory.velocity}` : report.trajectory.velocity) : '0.00'} SGPA
              </span>
            </div>

            <h2 className="text-xl md:text-2xl font-bold text-white leading-tight">
              {report?.trajectory?.trajectoryDescription || 'Your academic growth momentum is currently active.'}
            </h2>

            {report?.trajectory?.attendanceGradeCovarianceAlert ? (
              <div className="flex items-start gap-2.5 p-3 rounded-xl bg-amber-500/10 border border-amber-500/30 text-amber-200 text-xs">
                <AlertTriangle className="w-4 h-4 text-amber-400 shrink-0 mt-0.5" />
                <span>{report?.trajectory?.covarianceMessage}</span>
              </div>
            ) : (
              <div className="flex items-center gap-2 text-xs text-slate-400">
                <ShieldCheck className="w-4 h-4 text-emerald-400 shrink-0" />
                <span>{report?.trajectory?.covarianceMessage}</span>
              </div>
            )}
          </div>

          {/* Quick Stat Tiles */}
          <div className="grid grid-cols-3 gap-3 shrink-0">
            <div className="p-4 rounded-xl bg-slate-900/60 border border-slate-800/80 text-center min-w-[105px]">
              <span className="text-[11px] font-semibold text-slate-400 uppercase tracking-wider block">Current SGPA</span>
              <span className="text-2xl font-black text-white mt-1 block">{report?.trajectory?.currentSgpa || '7.50'}</span>
              <span className={`text-[11px] font-bold ${report?.trajectory?.velocity && report.trajectory.velocity >= 0 ? 'text-emerald-400' : 'text-rose-400'}`}>
                {report?.trajectory?.velocity && report.trajectory.velocity >= 0 ? `+${report.trajectory.velocity}` : report?.trajectory?.velocity} vs Prev
              </span>
            </div>

            <div className="p-4 rounded-xl bg-slate-900/60 border border-slate-800/80 text-center min-w-[105px]">
              <span className="text-[11px] font-semibold text-slate-400 uppercase tracking-wider block">Cumulative CGPA</span>
              <span className="text-2xl font-black text-indigo-300 mt-1 block">{report?.trajectory?.overallCgpa || '7.65'}</span>
              <span className="text-[11px] font-medium text-slate-400">All Semesters</span>
            </div>

            <div className="p-4 rounded-xl bg-slate-900/60 border border-slate-800/80 text-center min-w-[105px]">
              <span className="text-[11px] font-semibold text-slate-400 uppercase tracking-wider block">Momentum Index</span>
              <span className="text-2xl font-black text-amber-400 mt-1 block">
                {report?.trajectory?.momentumScore ? (report.trajectory.momentumScore > 0 ? `+${report.trajectory.momentumScore}` : report.trajectory.momentumScore) : '+45'}
              </span>
              <span className="text-[11px] font-medium text-slate-400">Scale (-100 to +100)</span>
            </div>
          </div>
        </div>
      </div>

      {/* Longitudinal Semester Progression Timeline */}
      <div className="space-y-4">
        <div className="flex items-center justify-between">
          <h3 className="text-base font-bold text-white flex items-center gap-2">
            <Compass className="w-4 h-4 text-indigo-400" />
            Longitudinal Academic Timeline
          </h3>
          <span className="text-xs text-slate-400">Multi-Semester Progression</span>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          {report?.trajectory?.semesterHistory?.map((sem) => (
            <div
              key={sem.semesterNumber}
              className="p-5 rounded-xl bg-slate-900/60 border border-slate-800/80 hover:border-indigo-500/30 transition-all space-y-3"
            >
              <div className="flex items-center justify-between">
                <span className="text-xs font-bold text-slate-300 uppercase tracking-wider">{sem.semesterName}</span>
                <span
                  className={`text-[11px] font-bold px-2 py-0.5 rounded-md ${
                    sem.attendancePercentage >= 75
                      ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20'
                      : 'bg-rose-500/10 text-rose-400 border border-rose-500/20'
                  }`}
                >
                  {sem.attendancePercentage}% Attd
                </span>
              </div>

              <div className="flex items-baseline justify-between pt-1">
                <div>
                  <span className="text-2xl font-black text-white">{sem.sgpa}</span>
                  <span className="text-xs text-slate-400 ml-1.5 font-medium">SGPA</span>
                </div>
                <span className="text-xs text-slate-400">{sem.credits} Credits</span>
              </div>

              {/* Attendance Mini Bar */}
              <div className="space-y-1 pt-1">
                <div className="w-full bg-slate-800 rounded-full h-1.5 overflow-hidden">
                  <div
                    className={`h-full rounded-full transition-all ${
                      sem.attendancePercentage >= 75 ? 'bg-gradient-to-r from-emerald-500 to-teal-400' : 'bg-rose-500'
                    }`}
                    style={{ width: `${Math.min(100, sem.attendancePercentage)}%` }}
                  />
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Pillar 2: 5-Tier Subject Domain Pattern Recognition */}
      <div className="space-y-4">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-2">
          <div>
            <h3 className="text-base font-bold text-white flex items-center gap-2">
              <Brain className="w-4 h-4 text-purple-400" />
              Cognitive Domain Affinity & Pattern Recognition
            </h3>
            <p className="text-xs text-slate-400 mt-0.5">
              Subject proficiency mapped across 5 canonical industry clusters to identify cognitive strengths vs friction points.
            </p>
          </div>

          <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-xl bg-purple-500/10 border border-purple-500/20 text-purple-300 text-xs font-semibold">
            <Sparkles className="w-3.5 h-3.5" />
            Archetype: {report?.domainAffinity?.archetype || 'Hands-On Systems & Product Builder'}
          </div>
        </div>

        {/* Archetype Explanation */}
        <div className="p-4 rounded-xl bg-slate-900/40 border border-slate-800/80 text-xs text-slate-300 leading-relaxed">
          {report?.domainAffinity?.archetypeDescription ||
            'High natural affinity for practical software engineering, web platforms, and programming labs. Experiences cognitive friction primarily with abstract theoretical math proofs.'}
        </div>

        {/* Domain Cluster Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {report?.domainAffinity?.clusterBreakdown?.map((item) => (
            <div
              key={item.cluster}
              className="p-5 rounded-xl bg-slate-900/60 border border-slate-800/80 hover:border-slate-700/80 transition-all space-y-3"
            >
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-2">
                  {getClusterIcon(item.cluster)}
                  <span className="text-xs font-bold text-slate-200">{item.displayName}</span>
                </div>
                <span
                  className={`text-[10px] font-bold px-2 py-0.5 rounded-md uppercase tracking-wider ${
                    item.status === 'STRENGTH'
                      ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20'
                      : item.status === 'FRICTION_POINT'
                      ? 'bg-rose-500/10 text-rose-400 border border-rose-500/20'
                      : 'bg-blue-500/10 text-blue-400 border border-blue-500/20'
                  }`}
                >
                  {item.status === 'STRENGTH' ? 'Core Strength' : item.status === 'FRICTION_POINT' ? 'Friction Point' : 'Balanced'}
                </span>
              </div>

              <div className="flex items-baseline justify-between pt-1">
                <span className="text-2xl font-black text-white">{item.averageScore}%</span>
                <span className="text-xs text-slate-400">Affinity Index: {item.affinityIndex}x</span>
              </div>

              <div className="w-full bg-slate-800 rounded-full h-2 overflow-hidden">
                <div
                  className={`h-full rounded-full transition-all ${
                    item.status === 'STRENGTH'
                      ? 'bg-gradient-to-r from-emerald-500 to-teal-400'
                      : item.status === 'FRICTION_POINT'
                      ? 'bg-gradient-to-r from-rose-500 to-orange-400'
                      : 'bg-gradient-to-r from-blue-500 to-indigo-400'
                  }`}
                  style={{ width: `${Math.min(100, item.averageScore)}%` }}
                />
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Pillar 3: Pragmatic Industry-Aligned Remediation Framework (PIARF) */}
      <div className="space-y-4">
        <div>
          <h3 className="text-base font-bold text-white flex items-center gap-2">
            <Layers className="w-4 h-4 text-amber-400" />
            Pragmatic Industry-Aligned Remediation Framework
          </h3>
          <p className="text-xs text-slate-400 mt-0.5">
            Clear triage between high-ROI core CS remediation and low-ROI pass-only clearance to protect your coding bandwidth.
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Column 1: High-ROI Core (Critical Focus) */}
          <div className="space-y-3">
            <div className="flex items-center gap-2 text-xs font-bold text-rose-400 uppercase tracking-wider">
              <Flame className="w-4 h-4 text-rose-400" />
              High-ROI Core Subjects (Critical Remediation)
            </div>

            {criticalRemediations.length === 0 ? (
              <div className="p-5 rounded-xl bg-slate-900/40 border border-slate-800 text-slate-400 text-xs">
                No critical core subjects flagged! All foundational CS courses are in good standing.
              </div>
            ) : (
              criticalRemediations.map((item) => (
                <div
                  key={item.subjectCode}
                  className="p-5 rounded-xl bg-gradient-to-br from-rose-950/20 to-slate-900/80 border border-rose-500/30 space-y-3 shadow-lg"
                >
                  <div className="flex items-center justify-between">
                    <div>
                      <span className="text-xs font-bold text-white block">{item.subjectName}</span>
                      <span className="text-[11px] text-slate-400">{item.subjectCode} • Score: {item.scoreOrGrade}</span>
                    </div>
                    <span className="px-2.5 py-1 text-[10px] font-extrabold rounded-lg bg-rose-500/20 text-rose-400 border border-rose-500/30 uppercase tracking-wider">
                      Priority 1
                    </span>
                  </div>

                  <div className="p-3 rounded-lg bg-rose-950/30 border border-rose-500/20 text-xs text-rose-200 leading-relaxed">
                    <strong>Root Cause:</strong> {item.rootCauseExplanation}
                  </div>

                  <div className="text-xs text-slate-300 leading-relaxed">
                    <strong>Industry Directive:</strong> {item.pragmaticAdvice}
                  </div>

                  <div className="pt-1 flex items-center justify-between text-[11px] text-slate-400">
                    <span>{item.industryContext}</span>
                    <Link
                      href={`/dashboard/student/chatbot?query=Help me remediate my low score in ${encodeURIComponent(item.subjectName)}`}
                      className="text-indigo-400 hover:text-indigo-300 font-medium inline-flex items-center gap-1"
                    >
                      Remediate with AI <ArrowRight className="w-3 h-3" />
                    </Link>
                  </div>
                </div>
              ))
            )}
          </div>

          {/* Column 2: Low-ROI Auxiliary (Pass-Only Clearance) */}
          <div className="space-y-3">
            <div className="flex items-center gap-2 text-xs font-bold text-slate-300 uppercase tracking-wider">
              <ShieldCheck className="w-4 h-4 text-blue-400" />
              Low-ROI Auxiliary Courses (Pass-Only Strategy)
            </div>

            {passOnlyRemediations.length === 0 ? (
              <div className="p-5 rounded-xl bg-slate-900/40 border border-slate-800 text-slate-400 text-xs">
                No auxiliary backlogs or low marks flagged.
              </div>
            ) : (
              passOnlyRemediations.map((item) => (
                <div
                  key={item.subjectCode}
                  className="p-5 rounded-xl bg-slate-900/60 border border-slate-700/60 space-y-3"
                >
                  <div className="flex items-center justify-between">
                    <div>
                      <span className="text-xs font-bold text-white block">{item.subjectName}</span>
                      <span className="text-[11px] text-slate-400">{item.subjectCode} • Score: {item.scoreOrGrade}</span>
                    </div>
                    <span className="px-2.5 py-1 text-[10px] font-bold rounded-lg bg-slate-800 text-slate-300 border border-slate-700 uppercase tracking-wider">
                      Pass-Only
                    </span>
                  </div>

                  <div className="p-3 rounded-lg bg-slate-800/50 border border-slate-700/50 text-xs text-slate-300 leading-relaxed">
                    <strong>Pragmatic Advice:</strong> {item.pragmaticAdvice}
                  </div>

                  <div className="text-[11px] text-slate-400 italic">
                    {item.industryContext}
                  </div>
                </div>
              ))
            )}
          </div>
        </div>
      </div>

      {/* Pillar 4: Socratic Conversational Prompts for Chatbot */}
      <div className="p-6 rounded-2xl bg-gradient-to-r from-indigo-950/40 via-purple-950/20 to-slate-900 border border-indigo-500/30 space-y-4 shadow-xl">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2.5">
            <Bot className="w-5 h-5 text-indigo-400" />
            <h4 className="text-sm font-bold text-white">Ask Senior Tech Mentor (AI Chatbot)</h4>
          </div>
          <span className="text-xs text-indigo-300/80 font-medium">Pre-loaded with your Growth Trajectory</span>
        </div>

        <p className="text-xs text-slate-300">
          Click any prompt below to launch the AI Chatbot with your full academic momentum and subject affinity context pre-injected:
        </p>

        <div className="flex flex-wrap gap-2.5">
          <button
            onClick={() =>
              router.push(
                `/dashboard/student/chatbot?query=${encodeURIComponent(
                  'Based on my current academic trajectory, what software engineering projects should I prioritize this semester?'
                )}`
              )
            }
            className="px-3.5 py-2 rounded-xl text-xs font-medium text-slate-200 bg-slate-800/80 hover:bg-slate-700/80 border border-slate-700/80 transition-all flex items-center gap-1.5 shadow-sm"
          >
            🚀 Best projects for my archetype <ArrowRight className="w-3 h-3 text-indigo-400" />
          </button>

          <button
            onClick={() =>
              router.push(
                `/dashboard/student/chatbot?query=${encodeURIComponent(
                  'How should I clear low-ROI auxiliary subjects like EVS without wasting my core coding hours?'
                )}`
              )
            }
            className="px-3.5 py-2 rounded-xl text-xs font-medium text-slate-200 bg-slate-800/80 hover:bg-slate-700/80 border border-slate-700/80 transition-all flex items-center gap-1.5 shadow-sm"
          >
            🛡️ 2-day clearance strategy for non-core subjects <ArrowRight className="w-3 h-3 text-indigo-400" />
          </button>

          <button
            onClick={() =>
              router.push(
                `/dashboard/student/chatbot?query=${encodeURIComponent(
                  'Analyze the correlation between my attendance and my marks across recent semesters.'
                )}`
              )
            }
            className="px-3.5 py-2 rounded-xl text-xs font-medium text-slate-200 bg-slate-800/80 hover:bg-slate-700/80 border border-slate-700/80 transition-all flex items-center gap-1.5 shadow-sm"
          >
            📊 Attendance vs Marks correlation <ArrowRight className="w-3 h-3 text-indigo-400" />
          </button>
        </div>
      </div>
    </div>
  );
}
