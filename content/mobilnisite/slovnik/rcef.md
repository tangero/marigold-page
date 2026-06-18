---
slug: "rcef"
url: "/mobilnisite/slovnik/rcef/"
type: "slovnik"
title: "RCEF – RRC Connection Establishment Failure"
date: 2026-01-01
abbr: "RCEF"
fullName: "RRC Connection Establishment Failure"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/rcef/"
summary: "Klíčový ukazatel výkonnosti (KPI) měřící míru neúspěšnosti pokusů UE o navázání spojení řízení rádiových prostředků (Radio Resource Control, RRC) se sítí. Je klíčový pro monitorování dostupnosti sítě"
---

RCEF je klíčový ukazatel výkonnosti měřící míru neúspěšnosti pokusů uživatelského zařízení o navázání spojení řízení rádiových prostředků (Radio Resource Control) se sítí.

## Popis

[RRC](/mobilnisite/slovnik/rrc/) Connection Establishment Failure (RCEF) je kritické měření výkonnosti definované ve specifikacích 3GPP pro správu a optimalizaci sítě. Kvantifikuje podíl neúspěšných pokusů uživatelského zařízení (UE) o přechod ze stavu RRC_IDLE nebo RRC_INACTIVE do stavu RRC_CONNECTED. Proces navazování je zahájen odesláním zprávy RRCConnectionRequest ze strany UE, typicky vyvolané událostmi jako počáteční přístup, mobilně iniciovaný přenos dat nebo odpověď na stránkovací zprávu. Síť odpoví zprávou RRCConnectionSetup, pokud jsou k dispozici prostředky a podmínky to umožňují. K selhání se započítá, pokud se tento proces úspěšně nedokončí a UE nevstoupí do připojeného stavu.

K selhání může dojít z různých důvodů kategorizovaných ve specifikacích. Mezi běžné příčiny patří selhání rádiového spoje během procedury, jako je špatná kvalita signálu (např. nízká [RSRP](/mobilnisite/slovnik/rsrp/)/[RSRQ](/mobilnisite/slovnik/rsrq/)), vysoké rušení nebo náhlé zhoršení signálu. Selhání mohou také pramenit z odmítnutí sítí, kdy [eNB](/mobilnisite/slovnik/enb/)/gNB odešle zprávu RRCConnectionReject, často kvůli přetížení, nedostatku rádiových prostředků nebo zásadám řízení přístupu. Mezi další příčiny patří vypršení časovačů (jako T300) před dokončením nastavení, selhání řešení kolizí na náhodných přístupových kanálech nebo interní problémy UE. Konkrétní příčiny selhání jsou často zaznamenávány pro podrobnou analýzu kořenové příčiny.

Z architektonického hlediska se RCEF měří v uzlu přístupové rádiové sítě (RAN) – eNB v LTE nebo gNB v 5G NR. Systém řízení shromažďuje tato měření prostřednictvím definovaných rozhraní a čítačů správy výkonnosti specifikovaných v dokumentech jako 32.421 a 32.422. Operátoři používají [KPI](/mobilnisite/slovnik/kpi/) RCEF k posouzení dostupnosti sítě, což je základní aspekt kvality služeb. Vysoké míry RCEF přímo ovlivňují uživatelský zážitek, protože zařízení se nemohou zaregistrovat nebo zahájit relace. Proto je nepřetržité monitorování a minimalizace RCEF ústředním bodem procesů plánování, optimalizace a odstraňování problémů v rádiové síti, což zajišťuje spolehlivý počáteční přístup pro účastníky.

## K čemu slouží

Účelem definice RCEF jako standardizovaného [KPI](/mobilnisite/slovnik/kpi/) je poskytnout operátorům konzistentní, kvantifikovatelnou metriku pro vyhodnocení a zajištění dostupnosti sítě. Před takovými standardizovanými měřeními se operátoři spoléhali na různé, dodavatelem specifické ukazatele, což ztěžovalo srovnávání sítí různých dodavatelů a holistickou optimalizaci. RCEF řeší potřebu objektivního měření toho, jak úspěšně se mohou uživatelé připojit k síti, což je základním krokem pro jakoukoli mobilní službu.

Jeho vytvoření bylo motivováno rostoucí složitostí mobilních sítí a kritickým významem dostupnosti služeb vnímané uživatelem. Jak se sítě vyvíjely prostřednictvím vydání 3GPP, podporovaly více zařízení a rozmanité služby, počáteční přístupová procedura se stala potenciálním úzkým hrdlem. Vysoké míry selhání mohly naznačovat základní problémy, jako jsou díry v pokrytí, nadměrné rušení, přetížení buňky nebo chybně nakonfigurované parametry. Standardizací RCEF umožnila 3GPP automatizovaným systémům správy výkonnosti tyto problémy efektivně detekovat, lokalizovat a pomáhat s jejich diagnostikou.

RCEF řeší problém neprůhledných selhání počátečního přístupu. Přeměňuje kritickou síťovou událost na měřitelný a akční KPI. To umožňuje operátorům nastavovat výkonnostní prahové hodnoty, spouštět alarmy a řídit optimalizační kampaně – jako je nastavení sklonu antén, úprava výkonu nebo ladění parametrů – za účelem zlepšení dostupnosti. V konečném důsledku přispívá k plnění smluv o úrovni služeb, snižování stížností zákazníků a zajištění spolehlivého prvního kontaktu mezi uživatelem a sítí.

## Klíčové vlastnosti

- Standardizovaný KPI pro měření dostupnosti sítě
- Pokrývá selhání během přechodu ze stavu RRC_IDLE/INACTIVE do stavu RRC_CONNECTED
- Podporuje kategorizaci příčin selhání (např. rádiové selhání, odmítnutí, vypršení časovače)
- Definované čítače správy výkonnosti pro sběr přes rozhraní OAM
- Aplikovatelné pro sítě LTE (eNB) i 5G NR (gNB)
- Používá se pro minimalizaci drive-testů a automatizovanou optimalizaci sítě

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)
- [KPI – Key Performance Indicators](/mobilnisite/slovnik/kpi/)

## Definující specifikace

- **TS 28.622** (Rel-20) — Telecommunication Management; Generic NRM Information Service
- **TS 28.627** (Rel-19) — SON Policy NRM IRP: Requirements
- **TR 28.837** (Rel-18) — Technical Report on Trace/MDT Management
- **TS 32.421** (Rel-19) — Subscriber & Equipment Trace Concepts & Requirements
- **TS 32.422** (Rel-20) — Telecom Management: Trace Control & Configuration
- **TS 32.442** (Rel-19) — Trace Management IRP: Information Service
- **TS 32.836** (Rel-12) — NM Centralized Coverage and Capacity Optimization Study

---

📖 **Anglický originál a plná specifikace:** [RCEF na 3GPP Explorer](https://3gpp-explorer.com/glossary/rcef/)
