---
slug: "ppp-rtk"
url: "/mobilnisite/slovnik/ppp-rtk/"
type: "slovnik"
title: "PPP-RTK – Precise Point Positioning – Real-Time Kinematic"
date: 2025-01-01
abbr: "PPP-RTK"
fullName: "Precise Point Positioning – Real-Time Kinematic"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ppp-rtk/"
summary: "PPP-RTK je pokročulá služba vysoce přesného určování polohy pro 5G NR a LTE, která kombinuje satelitní Precise Point Positioning (PPP) s kinematickými korekcemi v reálném čase (RTK). Poskytuje přesnos"
---

PPP-RTK je pokročilá služba vysoce přesného určování polohy pro 5G NR a LTE, která kombinuje satelitní Precise Point Positioning s kinematickými korekcemi v reálném čase (Real-Time Kinematic) doručovanými přes mobilní síť, čímž dosahuje přesnosti na úrovni centimetrů.

## Popis

Precise Point Positioning – Real-Time Kinematic (PPP-RTK) je technologie vysoce přesného určování polohy standardizovaná 3GPP pro integraci do buněčných sítí, konkrétně pro LTE a 5G NR. Představuje spojení dvě zavedených technik vylepšení [GNSS](/mobilnisite/slovnik/gnss/): Precise Point Positioning ([PPP](/mobilnisite/slovnik/ppp/)), která využívá přesná data korekcí satelitních drah a hodin ke zlepšení přesnosti jednoho přijímače, a Real-Time Kinematic ([RTK](/mobilnisite/slovnik/rtk/)), která využívá měření fáze nosné a korekce z referenční stanice k dosažení přesnosti na úrovni centimetrů. Systém 3GPP definuje architekturu a protokoly pro doručování potřebných PPP-RTK korekčních dat (včetně drah, hodin, biasů a atmosférických zpoždění) od poskytovatele korekční služby ke koncovému zařízení (UE) přes uživatelskou nebo řídicí rovinu mobilní sítě.

Architektura zahrnuje několik klíčových komponent. Síť referenčních stanic GNSS sbírá nezpracovaná satelitní měření. PPP-RTK server tato data zpracuje a vygeneruje korekce ve formátu stavového prostoru ([SSR](/mobilnisite/slovnik/ssr/)). Tyto korekce jsou pak naformátovány podle protokolů definovaných 3GPP (např. pomocí rozhraní LPPa nebo [SUPL](/mobilnisite/slovnik/supl/)) a doručeny do UE. Doručení může probíhat přes signalizaci typu point-to-point pomocí protokolu LTE Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)) nebo New Radio Positioning Protocol A (NRPPa), nebo přes broadcastové/multicastové metody. UE, vybavené přijímačem GNSS, přijímá jak standardní satelitní signály, tak síťové korekce. Tyto korekce pak aplikuje ve svém polohovacím enginu, aby vyřešila celočíselné nejednoznačnosti v měření fáze nosné, což jí umožňuje vypočítat svou polohu s extrémně vysokou přesností (až na několik centimetrů) v reálném čase.

Fungování PPP-RTK je vícekrokový proces. Nejprve UE naváže sítí relaci určování polohy, případně indikuje svou schopnost a zájem o službu vysoké přesnosti. Funkce Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)) nebo Secure User Plane Location (SUPL) Location Platform ([SLP](/mobilnisite/slovnik/slp/)) v síti získá příslušná korekční data od poskytovatele služby. Tato data jsou přenesena do UE, která je použije ke korekci systematických chyb ve svých GNSS měřeních. Klíčovou výhodou oproti tradičnímu RTK je škálovatelnost; zatímco klasické RTK vyžaduje blízkou referenční stanici (což omezuje dosah), PPP-RTK využívá korekce stavového prostoru, které jsou platné na mnohem větší oblasti, čímž snižuje hustotu potřebné infrastruktury. Její role v systému 5G je klíčová pro podporu pokročilých aplikací V2X, průmyslového IoT a rozšířené reality, které vyžadují přesné, spolehlivé a všudypřítomné určování polohy, což z ní činí klíčový enabler pro digitální transformaci vertikálních odvětví.

## K čemu slouží

PPP-RTK bylo vytvořeno, aby splnilo přísné požadavky na určování polohy vznikajících případů užití 5G, které standardní GNSS nebo asistované GNSS (A-GNSS) nemohou uspokojit. Aplikace jako autonomní vozidla, precizní zemědělství, doručování pomocí dronů a chytrá výstavba vyžadují kontinuální, spolehlivou, centimetrovou přesnost. Tradiční RTK poskytuje vysokou přesnost, ale má omezenou oblast pokrytí (typicky < 20 km od referenční stanice) a vyžaduje hustou infrastrukturu. Standardní PPP nabízí širokoplošné pokrytí, ale může mít dlouhou dobu konvergence (desítky minut), než dosáhne centimetrové přesnosti. PPP-RTK kombinuje to nejlepší z obou: širokoplošnou platnost PPP s rychlou konvergencí a vysokou přesností RTK.

Motivací pro jeho standardizaci v 3GPP (počínaje Release 16) byly požadavky automobilového a průmyslového sektoru. Omezení předchozích přístupů – buď nedostatečná přesnost (A-GNSS), nebo nepraktické náklady na infrastrukturu a mezery v pokrytí (tradiční RTK sítě) – představovala významné překážky. Využitím všudypřítomného pokrytí a spolehlivé datové konektivity 5G sítí pro doručování korekcí PPP-RTK řeší problémy škálovatelnosti a doby konvergence. To umožňuje poskytovatelům služeb nabízet hromadnou službu vysoce přesného určování polohy, která je základním stavebním kamenem pro budoucnost autonomních systémů a Průmyslového internetu věcí (IIoT), čímž naplňuje mandát 3GPP podporovat potřeby vertikálních odvětví.

## Klíčové vlastnosti

- Poskytuje přesnost určování polohy na úrovni centimetrů v reálném čase
- Využívá korekční data ve formátu stavového prostoru (State-Space Representation – SSR)
- Podporuje doručování přes řídicí rovinu (LPP/NRPPa) i uživatelskou rovinu (SUPL)
- Umožňuje širokoplošné pokrytí s rychlejší konvergencí než standardní PPP
- Integruje se s architekturou 5G sítě pro spolehlivé doručování korekcí
- Klíčový enabler pro V2X, autonomní systémy a průmyslovou automatizaci

## Definující specifikace

- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [PPP-RTK na 3GPP Explorer](https://3gpp-explorer.com/glossary/ppp-rtk/)
