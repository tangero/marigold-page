---
slug: "snr"
url: "/mobilnisite/slovnik/snr/"
type: "slovnik"
title: "SNR – Spending Status Notification Request"
date: 2025-01-01
abbr: "SNR"
fullName: "Spending Status Notification Request"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/snr/"
summary: "Spending Status Notification Request (SN-Request, Žádost o notifikaci stavu čerpání) je protokolový prvek používaný v CAMEL (Customised Applications for Mobile network Enhanced Logic) k aktivaci notif"
---

SNR je prvek protokolu CAMEL používaný k aktivaci notifikací o spotřebě předplaceného kreditu účastníka, což umožňuje řízení dobíjení a upozornění v reálném čase v mobilních sítích.

## Popis

Spending Status Notification Request (SN-Request, Žádost o notifikaci stavu čerpání) je specifická operace v rámci sady protokolů [CAMEL](/mobilnisite/slovnik/camel/) (Customised Applications for Mobile network Enhanced Logic), což je standard 3GPP pro služby inteligentní sítě ([IN](/mobilnisite/slovnik/in/)) v sítích GSM, UMTS a novějších. CAMEL umožňuje operátorům sítí nasazovat vlastní služby, jako je předplacené účtování, překlad čísel nebo filtrování hovorů. SN-Request je zpráva odeslaná z Service Control Point ([SCP](/mobilnisite/slovnik/scp/)) sítě – který hostuje služební logiku pro předplacené služby – do Service Switching Point ([SSP](/mobilnisite/slovnik/ssp/)), typicky Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo Gateway MSC. Jejím účelem je instruovat SSP, aby monitoroval hovor nebo relaci účastníka a odeslal notifikaci zpět do SCP, když zůstatek na účtu účastníka dosáhne během komunikace určitých předdefinovaných prahových hodnot.

Jak to funguje, je nedílnou součástí předplaceného účtování v reálném čase. Když předplacený účastník zahájí hovor, MSC/SSP detekuje CAMEL aktivovaný hovor a pozastaví jeho zpracování. Odešle zprávu InitialDP do SCP. SCP po zkontrolování zůstatku účastníka a ocenění hovoru autorizuje hovor na počáteční dobu trvání. Zásadní je, že SCP může do své odpovědi (např. v operaci RequestReportBCSMEvent nebo ApplyCharging) zahrnout SN-Request. Tato žádost obsahuje parametry, jako jsou prahové hodnoty limitu čerpání (např. upozornit při využití 50 % přiděleného kreditu a znovu při 80 %). Jak hovor pokračuje, MSC/SSP sleduje dobu jeho trvání nebo objem dat. Při překročení určeného prahu odešle SSP notifikaci (EventReportBCSM nebo ApplyChargingReport) zpět do SCP.

Po přijetí notifikace může SCP podniknout další akci. Ta typicky zahrnuje novou kontrolu zůstatku účastníka, výpočet nové přidělené částky kreditu pro další segment hovoru a odeslání nové autorizace do SSP pro pokračování hovoru. Tento proces periodického oznamování a znovuautorizace pokračuje až do ukončení hovoru nebo vyčerpání kreditu. Mechanismus SN-Request je klíčový pro implementaci funkcí, jako jsou varování o nízkém zůstatku, kdy síť může přehrát účastníkovi hlášení, nebo řádné ukončení hovoru při vyčerpání prostředků. Zajišťuje, že předplacené účtování je přesné, probíhá v reálném čase a umožňuje interaktivní upozornění pro účastníka.

## K čemu slouží

SN-Request byl vyvinut, aby řešil zásadní výzvu řízení a notifikací v reálném čase u předplacených telefonních služeb. Před [CAMEL](/mobilnisite/slovnik/camel/) a mechanismy jako SN-Request byly předplacené služby často implementovány méně efektivními prostředky, jako je mezera mezi hovory (call gapping) nebo jednoduché limity délky bez podrobné kontroly. Tyto metody mohly vést k nespokojenosti účastníků kvůli náhlému ukončení hovoru bez varování nebo nepřesnému účtování. SN-Request poskytuje standardizovaný signalizační mechanismus během hovoru, který umožňuje systému účtování ([SCP](/mobilnisite/slovnik/scp/)) být informován o spotřebě prostředků.

Řeší problém proaktivní správy účtu během aktivní relace. Bez něj by SCP znal celkovou cenu až po skončení hovoru, což by riskovalo přečerpání. S SN-Request může SCP monitorovat čerpání přírůstkově, což umožňuje: 1) **Přesnou kontrolu kreditu**: Přidělování kreditu po částech zabraňuje účastníkům překročit jejich zůstatek. 2) **Vylepšený uživatelský zážitek**: Umožnění hlášení o nízkém zůstatku dává účastníkům šanci dobít kredit nebo hovor řádně ukončit. 3) **Flexibilní služební logiku**: Operátoři mohou definovat více prahových hodnot pro různé typy notifikací nebo akcí. Jeho vytvoření bylo motivováno masivním růstem předplacených mobilních tarifů, které vyžadovaly robustní, škálovatelné a funkčně bohaté systémy účtování schopné fungovat napříč různými síťovými prvky a dodavateli, což CAMEL a jeho podrobné operace, jako je SN-Request, poskytly.

## Klíčové vlastnosti

- Operace CAMEL používaná pro řízení předplaceného účtování v reálném čase
- Instruuje MSC/SSP, aby hlásil při dosažení předdefinovaných prahových hodnot spotřeby prostředků účastníka
- Umožňuje periodickou znovuautorizaci hovorů nebo relací na základě zbývajícího kreditu
- Podporuje upozornění účastníků, jako jsou varování o nízkém zůstatku prostřednictvím hlášení během hovoru
- Funguje v součinnosti s fázemi CAMEL a dalšími operacemi, jako je ApplyCharging
- Použitelná pro hlasové hovory, SMS a datové relace v kontextech GSM, UMTS a evolved packet core

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.484** (Rel-19) — MCS Configuration Management
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 26.094** (Rel-19) — AMR Voice Activity Detector (VAD) Specification
- **TS 26.881** (Rel-15) — MBMS FEC for Mission Critical Services Study
- **TR 26.918** (Rel-19) — Virtual Reality Relevance Study for 3GPP
- **TR 26.933** (Rel-19) — Study on Diverse Audio Capturing System
- **TR 26.943** (Rel-19) — SES Codec Selection Report
- **TR 26.952** (Rel-19) — EVS Codec Selection, Verification & Characterization
- **TR 26.975** (Rel-19) — AMR Speech Codec Performance Background
- **TR 26.976** (Rel-19) — AMR-WB Codec Characterization & Verification
- **TR 26.978** (Rel-19) — AMR Noise Suppression Selection Phase Technical Report
- **TR 26.997** (Rel-19) — IVAS Codec Specification
- … a dalších 44 specifikací

---

📖 **Anglický originál a plná specifikace:** [SNR na 3GPP Explorer](https://3gpp-explorer.com/glossary/snr/)
