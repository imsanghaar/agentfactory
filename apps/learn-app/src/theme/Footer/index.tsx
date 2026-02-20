import Link from "@docusaurus/Link";
import { Linkedin } from "lucide-react";
import { Button } from "@/components/ui/button";
import { siYoutube, siInstagram, siFacebook } from "simple-icons/icons";

export default function Footer() {
    const currentYear = new Date().getFullYear();

    return (
        <footer className="bg-background border-t border-border/50 text-foreground pt-16 pb-8 px-4 md:px-8 overflow-hidden font-sans">
            <div className="mx-auto max-w-[1800px]">
                {/* Top Section */}
                <div className="grid grid-cols-1 md:grid-cols-12 gap-12 mb-12">
                    {/* Brand / Newsletter - Spans 5 columns */}
                    <div className="md:col-span-5 flex flex-col justify-between h-full">
                        <div>
                            <h3 className="text-2xl font-semibold mb-6 tracking-tight">The AI Agent Factory</h3>
                        </div>
                    </div>

                    {/* Spacer Column */}
                    <div className="hidden md:block md:col-span-1"></div>

                    {/* Links - Spans 6 columns */}
                    <div className="md:col-span-6 grid grid-cols-1 gap-8 text-sm">
                        {/* Column 1 */}
                        <div className="flex flex-col gap-2">
                            <h4 className="font-bold text-muted-foreground uppercase tracking-widest text-sm mb-2">Learn</h4>
                            <Button variant="link" className="h-auto p-0 justify-start text-muted-foreground hover:text-foreground" asChild>
                                <Link to="/docs/preface-agent-native">Start Reading</Link>
                            </Button>
                            <Button variant="link" className="h-auto p-0 justify-start text-muted-foreground hover:text-foreground" asChild>
                                <Link to="/docs/preface-agent-native">Curriculum</Link>
                            </Button>
                            <Button variant="link" className="h-auto p-0 justify-start text-muted-foreground hover:text-foreground" asChild>
                                <Link to="https://github.com/imsanghaar/agentfactory/tree/main/specs">Specification</Link>
                            </Button>
                            <Button variant="link" className="h-auto p-0 justify-start text-muted-foreground hover:text-foreground" asChild>
                                <Link to="https://github.com/imsanghaar">Projects</Link>
                            </Button>
                            <Button variant="link" className="h-auto p-0 justify-start text-muted-foreground hover:text-foreground" asChild>
                                <Link to="/authors">Authors</Link>
                            </Button>
                        </div>
                    </div>
                </div>

                {/* BIG TYPE Section */}
                <div className="w-full pt-16 pb-12 overflow-hidden flex justify-center px-4 md:px-0">
                    <svg
                        viewBox="0 0 100 20"
                        className="w-full h-auto select-none pointer-events-none opacity-90"
                        aria-label="imsanghaar"
                    >
                        <text
                            x="50"
                            y="50%"
                            dominantBaseline="middle"
                            textAnchor="middle"
                            fill="currentColor"
                            className="font-light uppercase tracking-[-0.08em]"
                            style={{ fontSize: '15px', fontFamily: 'var(--font-sans)', transform: 'scaleY(0.95)' }}
                        >
                            IMSANGHAAR
                        </text>
                    </svg>
                </div>

                {/* Bottom Section */}
                <div className="flex flex-col md:flex-row justify-between items-center gap-6 pt-8 text-sm text-muted-foreground">
                    <div>
                        &copy; {currentYear} imsanghaar. Open Source Education.
                    </div>

                    <div className="flex gap-2">
                        <Button variant="ghost" size="icon" asChild>
                            <Link to="https://youtube.com/@imsanghaar" aria-label="YouTube">
                                <svg role="img" viewBox="0 0 24 24" className="w-4 h-4" fill="currentColor">
                                    <path d={siYoutube.path} />
                                </svg>
                            </Link>
                        </Button>
                        <Button variant="ghost" size="icon" asChild>
                            <Link to="https://linkedin.com/company/imsanghaar" aria-label="LinkedIn">
                                <Linkedin />
                            </Link>
                        </Button>
                        <Button variant="ghost" size="icon" asChild>
                            <Link to="https://instagram.com/imsanghaar" aria-label="Instagram">
                                <svg role="img" viewBox="0 0 24 24" className="w-4 h-4" fill="currentColor">
                                    <path d={siInstagram.path} />
                                </svg>
                            </Link>
                        </Button>
                        <Button variant="ghost" size="icon" asChild>
                            <Link to="https://facebook.com/imsanghaar" aria-label="Facebook">
                                <svg role="img" viewBox="0 0 24 24" className="w-4 h-4" fill="currentColor">
                                    <path d={siFacebook.path} />
                                </svg>
                            </Link>
                        </Button>
                    </div>
                </div>
            </div>
        </footer>
    );
}
