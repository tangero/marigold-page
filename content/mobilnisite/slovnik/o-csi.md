---
slug: "o-csi"
url: "/mobilnisite/slovnik/o-csi/"
type: "slovnik"
title: "O-CSI – Originating CAMEL Subscription Information"
date: 2025-01-01
abbr: "O-CSI"
fullName: "Originating CAMEL Subscription Information"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/o-csi/"
summary: "Profil účastníka uložený v HLR, který obsahuje spouštěcí informace potřebné pro řízení služby CAMEL u odchozích hovorů. Informuje MSC, kdy a jak kontaktovat externí uzel řízení služeb (gsmSCF), aby ap"
---

O-CSI je profil účastníka v HLR, který poskytuje spouštěcí informace pro aplikaci inteligentních síťových služeb založených na CAMEL, jako je předplacené účtování, na odchozí hovory účastníka.

## Popis

Originating [CAMEL](/mobilnisite/slovnik/camel/) Subscription Information (O-CSI) je klíčový datový prvek v profilu účastníka uložený v domovském registru polohy ([HLR](/mobilnisite/slovnik/hlr/)). Jedná se o sadu strukturovaných parametrů, která instruuje navštívené mobilní ústředně ([VMSC](/mobilnisite/slovnik/vmsc/)) nebo přístupové [MSC](/mobilnisite/slovnik/msc/) ([GMSC](/mobilnisite/slovnik/gmsc/)), jak vyvolat služby CAMEL (Customised Applications for Mobile networks Enhanced Logic) pro hovory iniciované účastníkem. Když se účastník registruje v síti nebo když je zahájen hovor, HLR odešle O-CSI obsluhující MSC jako součást účastnických dat v operaci [MAP](/mobilnisite/slovnik/map/) Insert Subscriber Data. O-CSI obsahuje adresu gsmSCF (uzlu řízení služeb CAMEL), služební klíč (Service Key) pro identifikaci konkrétního servisního logického programu a seznam bodů detekce spouštěče (Trigger Detection Points, TDPs) pro model základního stavu odchozího hovoru (Originating Basic Call State Model, [O-BCSM](/mobilnisite/slovnik/o-bcsm/)).

Při přijetí pokusu o mobilní odchozí hovor vyšetřuje funkce přepínání služeb (Service Switching Function, [SSF](/mobilnisite/slovnik/ssf/)) v MSC O-CSI. Pokud událost hovoru odpovídá aktivovanému TDP (např. DP2 'Collected_Info'), SSF pozastaví zpracování hovoru a zahájí dialog s určeným gsmSCF pomocí protokolu CAMEL Application Part (CAP). Odešle zprávu InitialDP obsahující služební klíč a podrobnosti o hovoru. gsmSCF použije služební klíč k výběru příslušné servisní logiky, která následně převezme kontrolu nad hovorem a může například instruovat MSC, aby pokračovala, připojila se k určitému číslu, aplikovala speciální účtování nebo ukončila hovor. O-CSI může také obsahovat parametry jako výchozí zacházení s hovorem (Default Call Handling), které určuje, zda má hovor pokračovat, nebo být blokován, pokud je gsmSCF nedostupný.

Struktura a obsah O-CSI se vyvíjely napříč releasy 3GPP, aby podporovaly složitější služby. Může zahrnovat více adres gsmSCF pro sdílení zátěže nebo redundanci, kritéria pro to, které TDP jsou aktivní, a indikátory pro specifické schopnosti, jako je potlačení hlasových oznámení. Je to základní kámen architektury CAMEL, který umožňuje oddělení servisní logiky od základního přepínání hovorů. Tím, že jsou tyto informace dynamicky spravovány v HLR a distribuovány do MSC, mohou operátoři nasazovat a upravovat služby na úrovni jednotlivých účastníků bez nutnosti rekonfigurace každé síťové ústředny, což poskytuje obrovskou flexibilitu pro nabízení personalizovaných inteligentních síťových služeb.

## K čemu slouží

O-CSI bylo vytvořeno za účelem umožnění nasazení účastnicky specifických, síťových inteligentních služeb standardizovaným a škálovatelným způsobem napříč sítěmi GSM a UMTS. Před CAMEL byla jakákoliv pokročilá logika zpracování hovorů typicky pevně zakódována do softwaru MSC, což ji činilo nepružnou a obtížně přizpůsobitelnou pro jednotlivé účastníky nebo aktualizovatelnou napříč vícevýrobkovou sítí. To omezovalo schopnost operátorů rychle zavádět služby jako předplacené účtování, které vyžaduje interakci v reálném čase s centrálním stavem účtu.

O-CSI tento problém řeší tím, že funguje jako mobilně specifický 'spouštěcí profil'. Přesouvá inteligenci *kdy* a *jak* vyvolat službu z ústředny do dat účastníka. To umožňuje centralizovanému bodu řízení služeb (gsmSCF) kontrolovat hovory pro jakéhokoliv účastníka kdekoliv v síti na základě spouštěčů definovaných v jeho O-CSI. Přímo řeší obchodní a technickou potřebu služeb předplaceného účtování v reálném čase, které se staly masivním hybatelem růstu mobilní komunikace. Bez O-CSI by implementace předplaceného účtování vyžadovala komplexní a proprietární integraci na každé MSC.

Dále O-CSI usnadnilo vytvoření živého ekosystému přidaných služeb. Tím, že poskytlo standardizovaný mechanismus pro spouštění externí kontroly, umožnilo operátorům a poskytovatelům služeb třetích stran vyvíjet služby nezávisle na dodavateli základní ústředny. Toto oddělení urychlilo inovace a umožnilo služby jako virtuální privátní sítě, správa podvodů, filtrování hovorů nebo služby založené na poloze. Jeho kontinuální vývoj napříč mnoha releasy 3GPP podtrhuje jeho zásadní roli při umožnění programovatelného řízení služeb v mobilních sítích.

## Klíčové vlastnosti

- Uloženo v HLR a staženo do MSC/VLR jako součást účastnických dat
- Obsahuje adresu gsmSCF (uzlu řízení služeb)
- Zahrnuje služební klíč (Service Key) pro identifikaci konkrétní servisní logiky
- Obsahuje seznam bodů detekce spouštěče (TDPs) pro O-BCSM
- Může definovat výchozí zacházení s hovorem (Default Call Handling) pro scénáře selhání SCF
- Umožňuje účastnicky specifické vyvolání služeb CAMEL v reálném čase

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [T-CSI – Terminating CAMEL Subscription Information](/mobilnisite/slovnik/t-csi/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [O-BCSM – Originating Basic Call State Model](/mobilnisite/slovnik/o-bcsm/)
- [CAP – CAMEL Application Part](/mobilnisite/slovnik/cap/)

## Definující specifikace

- **TR 21.978** (Rel-4) — CAMEL Control of VoIP Services Feasibility Study
- **TS 23.031** (Rel-19) — Fraud Information Gathering System (FIGS) - Stage 2
- **TS 23.035** (Rel-19) — Immediate Service Termination (IST) Stage 2
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.293** (Rel-19) — Proxy Function in Domestic Service Provider

---

📖 **Anglický originál a plná specifikace:** [O-CSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/o-csi/)
