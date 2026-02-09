#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ERPNext Expert Portfolio - Flask Application
Modern, Bilingual Portfolio Showcasing ERPNext Automation Excellence
"""

from flask import Flask, render_template, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# Portfolio Data
PORTFOLIO_DATA = {
    'en': {
        'title': 'ERPNext Automation Expert',
        'subtitle': 'Transforming Business Operations Through Intelligent Automation',
        'hero_title': 'From 5 Days to 8 Hours',
        'hero_subtitle': 'Real Results from Intelligent ERPNext Implementation',
        'hero_description': 'Reducing month-end closing time by 84% through custom automation workflows',
        'cta_primary': 'View Portfolio',
        'cta_secondary': 'Contact on WhatsApp',
        
        'stats': [
            {'value': '60-80%', 'label': 'Cost Reduction', 'icon': '💰'},
            {'value': '98%', 'label': 'Accuracy Rate', 'icon': '🎯'},
            {'value': '8 Hours', 'label': 'Month-End Closing', 'icon': '⚡'},
            {'value': '10x', 'label': 'Scalability', 'icon': '📈'}
        ],
        
        'timeline': {
            'title': 'The Transformation Journey',
            'subtitle': 'Four Strategic Phases to Operational Excellence',
            'phases': [
                {
                    'number': '01',
                    'title': 'Challenge Analysis',
                    'description': 'Identified critical pain points: 5-day closing cycles, 15% error rates, and manual bottlenecks draining resources.',
                    'icon': '🔍',
                    'metrics': ['5 Days Closing Time', '15% Error Rate', 'High Manual Overhead']
                },
                {
                    'number': '02',
                    'title': 'Automation Architecture',
                    'description': 'Designed custom ERPNext workflows with real-time data processing, eliminating batch operations and human errors.',
                    'icon': '⚙️',
                    'metrics': ['Custom Workflows', 'Real-time Processing', 'Zero Manual Entry']
                },
                {
                    'number': '03',
                    'title': 'Implementation',
                    'description': 'Deployed scalable system with intelligent automation, seamless integrations, and enterprise-grade performance.',
                    'icon': '🚀',
                    'metrics': ['Full Integration', 'Staff Training', 'Performance Optimization']
                },
                {
                    'number': '04',
                    'title': 'Results Achieved',
                    'description': 'Delivered 84% time reduction, 98% accuracy, and 10x scalability without additional headcount.',
                    'icon': '✨',
                    'metrics': ['8 Hour Closing', '<2% Error Rate', '10x Growth Ready']
                }
            ]
        },
        
        'features': [
            {
                'title': 'Intelligent Automation',
                'description': 'Custom workflows that transform manual processes into self-operating systems',
                'icon': '🤖'
            },
            {
                'title': 'Real-Time Processing',
                'description': 'From hours to seconds - instant data processing and decision making',
                'icon': '⚡'
            },
            {
                'title': 'Error Prevention',
                'description': 'Reduced human errors from 15% to less than 2% through automation',
                'icon': '🎯'
            },
            {
                'title': 'Scalable Growth',
                'description': 'Handle 10x business growth without proportional cost increase',
                'icon': '📈'
            },
            {
                'title': 'Cost Optimization',
                'description': '60-80% reduction in operational time and resource allocation',
                'icon': '💰'
            },
            {
                'title': 'Enterprise Security',
                'description': 'Bank-level security with role-based access and audit trails',
                'icon': '🔒'
            }
        ],
        
        'tech_stack': {
            'title': 'Technology Excellence',
            'subtitle': 'Enterprise-grade tools for world-class results',
            'technologies': [
                {'name': 'ERPNext', 'category': 'ERP Platform', 'icon': '🏢'},
                {'name': 'Python', 'category': 'Backend Development', 'icon': '🐍'},
                {'name': 'Frappe Framework', 'category': 'Framework', 'icon': '⚙️'},
                {'name': 'n8n', 'category': 'Workflow Automation', 'icon': '🔄'},
                {'name': 'PostgreSQL/MariaDB', 'category': 'Database', 'icon': '💾'},
                {'name': 'Docker', 'category': 'DevOps', 'icon': '🐋'},
                {'name': 'REST APIs', 'category': 'Integration', 'icon': '🔌'},
                {'name': 'Git', 'category': 'Version Control', 'icon': '📦'}
            ]
        },
        
        'cta_section': {
            'title': 'Ready to Transform Your Business?',
            'subtitle': 'Let\'s discuss how automation can revolutionize your operations',
            'description': 'With proven expertise in ERPNext implementation and custom automation across Egypt, Saudi Arabia, and the Gulf region, I deliver measurable results that transform business operations.',
            'portfolio_btn': 'Explore Portfolio',
            'whatsapp_btn': 'Connect on WhatsApp'
        },
        
        'footer': {
            'tagline': 'Building Tomorrow\'s Business Systems Today',
            'links': {
                'portfolio': 'Portfolio',
                'github': 'GitHub',
                'linkedin': 'LinkedIn',
                'whatsapp': 'WhatsApp'
            }
        }
    },
    
    'ar': {
        'title': 'خبير أتمتة ERPNext',
        'subtitle': 'تحويل العمليات التجارية من خلال الأتمتة الذكية',
        'hero_title': 'من 5 أيام إلى 8 ساعات',
        'hero_subtitle': 'نتائج حقيقية من تطبيق ERPNext الذكي',
        'hero_description': 'تقليل وقت الإغلاق الشهري بنسبة 84% من خلال سير عمل مخصص',
        'cta_primary': 'عرض الأعمال',
        'cta_secondary': 'تواصل عبر واتساب',
        
        'stats': [
            {'value': '60-80%', 'label': 'خفض التكاليف', 'icon': '💰'},
            {'value': '98%', 'label': 'نسبة الدقة', 'icon': '🎯'},
            {'value': '8 ساعات', 'label': 'الإغلاق الشهري', 'icon': '⚡'},
            {'value': '10 أضعاف', 'label': 'قابلية التوسع', 'icon': '📈'}
        ],
        
        'timeline': {
            'title': 'رحلة التحول الرقمي',
            'subtitle': 'أربع مراحل استراتيجية نحو التميز التشغيلي',
            'phases': [
                {
                    'number': '٠١',
                    'title': 'تحليل التحديات',
                    'description': 'تحديد نقاط الضعف الحرجة: دورات إغلاق 5 أيام، معدل خطأ 15%، واختناقات يدوية تستنزف الموارد.',
                    'icon': '🔍',
                    'metrics': ['5 أيام وقت الإغلاق', '15% معدل الخطأ', 'عبء يدوي مرتفع']
                },
                {
                    'number': '٠٢',
                    'title': 'معمارية الأتمتة',
                    'description': 'تصميم سير عمل ERPNext مخصص مع معالجة البيانات الفورية، والقضاء على العمليات اليدوية والأخطاء البشرية.',
                    'icon': '⚙️',
                    'metrics': ['سير عمل مخصص', 'معالجة فورية', 'صفر إدخال يدوي']
                },
                {
                    'number': '٠٣',
                    'title': 'التنفيذ',
                    'description': 'نشر نظام قابل للتوسع مع أتمتة ذكية، تكاملات سلسة، وأداء على مستوى المؤسسات.',
                    'icon': '🚀',
                    'metrics': ['تكامل كامل', 'تدريب الموظفين', 'تحسين الأداء']
                },
                {
                    'number': '٠٤',
                    'title': 'النتائج المحققة',
                    'description': 'تحقيق خفض 84% في الوقت، دقة 98%، وقابلية توسع 10 أضعاف بدون زيادة في العمالة.',
                    'icon': '✨',
                    'metrics': ['8 ساعات إغلاق', '<2% معدل الخطأ', 'جاهز للنمو 10 أضعاف']
                }
            ]
        },
        
        'features': [
            {
                'title': 'الأتمتة الذكية',
                'description': 'سير عمل مخصص يحول العمليات اليدوية إلى أنظمة ذاتية التشغيل',
                'icon': '🤖'
            },
            {
                'title': 'المعالجة الفورية',
                'description': 'من ساعات إلى ثوانٍ - معالجة فورية للبيانات واتخاذ القرارات',
                'icon': '⚡'
            },
            {
                'title': 'منع الأخطاء',
                'description': 'تقليل الأخطاء البشرية من 15% إلى أقل من 2% من خلال الأتمتة',
                'icon': '🎯'
            },
            {
                'title': 'النمو القابل للتوسع',
                'description': 'التعامل مع 10 أضعاف النمو التجاري بدون زيادة متناسبة في التكلفة',
                'icon': '📈'
            },
            {
                'title': 'تحسين التكاليف',
                'description': 'خفض 60-80% في الوقت التشغيلي وتخصيص الموارد',
                'icon': '💰'
            },
            {
                'title': 'الأمان على مستوى المؤسسات',
                'description': 'أمان بمستوى البنوك مع صلاحيات متدرجة وسجلات مراجعة',
                'icon': '🔒'
            }
        ],
        
        'tech_stack': {
            'title': 'التميز التقني',
            'subtitle': 'أدوات على مستوى المؤسسات لنتائج عالمية',
            'technologies': [
                {'name': 'ERPNext', 'category': 'منصة ERP', 'icon': '🏢'},
                {'name': 'Python', 'category': 'تطوير الخادم', 'icon': '🐍'},
                {'name': 'Frappe Framework', 'category': 'إطار العمل', 'icon': '⚙️'},
                {'name': 'n8n', 'category': 'أتمتة سير العمل', 'icon': '🔄'},
                {'name': 'PostgreSQL/MariaDB', 'category': 'قاعدة البيانات', 'icon': '💾'},
                {'name': 'Docker', 'category': 'DevOps', 'icon': '🐋'},
                {'name': 'REST APIs', 'category': 'التكامل', 'icon': '🔌'},
                {'name': 'Git', 'category': 'إدارة الإصدارات', 'icon': '📦'}
            ]
        },
        
        'cta_section': {
            'title': 'هل أنت مستعد لتحويل عملك؟',
            'subtitle': 'دعنا نناقش كيف يمكن للأتمتة أن تُحدث ثورة في عملياتك',
            'description': 'مع خبرة مثبتة في تنفيذ ERPNext والأتمتة المخصصة عبر مصر والسعودية ودول الخليج، أقدم نتائج قابلة للقياس تحول العمليات التجارية.',
            'portfolio_btn': 'استكشف الأعمال',
            'whatsapp_btn': 'تواصل عبر واتساب'
        },
        
        'footer': {
            'tagline': 'نبني أنظمة أعمال الغد اليوم',
            'links': {
                'portfolio': 'الأعمال',
                'github': 'GitHub',
                'linkedin': 'LinkedIn',
                'whatsapp': 'واتساب'
            }
        }
    }
}

@app.route('/')
def index():
    """Main landing page"""
    # Get browser language
    browser_lang = request.accept_languages.best_match(['ar', 'en']) or 'en'
    lang = request.args.get('lang', browser_lang)
    
    return render_template('index.html', 
                         data=PORTFOLIO_DATA.get(lang, PORTFOLIO_DATA['en']),
                         lang=lang,
                         current_year=datetime.now().year)

@app.route('/api/contact', methods=['POST'])
def contact():
    """Handle contact form submissions"""
    data = request.get_json()
    
    # In production, you would process this data
    # For now, just return success
    return jsonify({
        'status': 'success',
        'message': 'Message received successfully'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
