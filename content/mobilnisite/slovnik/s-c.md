---
slug: "s-c"
url: "/mobilnisite/slovnik/s-c/"
type: "slovnik"
title: "S/C – Split/Combine Function"
date: 2025-01-01
abbr: "S/C"
fullName: "Split/Combine Function"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/s-c/"
summary: "Funkce Split/Combine (S/C) je síťový prvek v IP Multimedia Subsystem (IMS), který spravuje rozdělování a spojování mediálních toků pro scénáře s více zařízeními a více přístupy. Umožňuje distribuci je"
---

S/C je síťový prvek IMS, který rozděluje a spojuje mediální toky za účelem distribuce jedné relace na více uživatelských zařízení nebo přístupových sítí.

## Popis

Funkce Split/Combine (S/C) je funkční entita v architektuře 3GPP IP Multimedia Subsystem (IMS), která hraje klíčovou roli v pokročilých komunikačních službách zahrnujících více koncových bodů nebo přístupových větví pro jednoho uživatele. Jejím hlavním úkolem je manipulace s mediálními proudy: dokáže rozdělit jeden příchozí mediální tok (např. audio, video) na více odchozích proudů směřujících k různým cílům, nebo naopak spojit více příchozích proudů do jednoho odchozího toku. Tato funkcionalita je ústřední pro služby specifikované v TS 23.202 ([PSS](/mobilnisite/slovnik/pss/) - IP Multimedia Subsystem (IMS) Service Continuity) a TS 23.910 (Circuit Switched ([CS](/mobilnisite/slovnik/cs/)) domain and IP Multimedia Subsystem (IMS) service interaction). S/C je typicky implementována jako součást Application Server ([AS](/mobilnisite/slovnik/as/)) nebo Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)) v rámci IMS core sítě.

Z architektonického hlediska S/C interaguje se Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) přes rozhraní IMS Service Control ([ISC](/mobilnisite/slovnik/isc/)). Když je vyvolána služba vyžadující rozdělení nebo spojení média (např. uživatel chce přijmout hovor na více zařízeních současně), S-CSCF přesměruje [SIP](/mobilnisite/slovnik/sip/) relaci na AS hostující logiku S/C. S/C pak funguje jako Back-to-Back User Agent ([B2BUA](/mobilnisite/slovnik/b2bua/)) a vloží se do mediální cesty. Používá výměnu nabídek a odpovědí Session Description Protocol (SDP) k navázání samostatných mediálních větví s každým zapojeným koncovým bodem. Pro operaci rozdělení, jako je Simultaneous Ringing, S/C přijímá médium od volající strany, replikuje jej a posílá kopie na všechna registrovaná zařízení uživatele. Pro operaci spojení přijímá proudy z více zdrojů, míchá je (v případě audia) a posílá jeden složený proud zamýšlenému příjemci.

Jak to funguje, zahrnuje přesné řízení směrování média a často i zpracování média. Ve scénáři rozdělení pro přesměrování hovoru nebo současné zvonění S/C typicky nemění obsah média; pouze jej replikuje a směruje. Avšak ve scénářích spojení, jako když uživatel přepne hovor z mobilního telefonu na hands-free sadu v autě při zachování aktivního mikrofonu mobilního telefonu, může S/C potřebovat provést mixování audia. Funkce je řízena servisní logikou, která určuje, kdy rozdělit nebo spojit na základě uživatelských preferencí, stavu sítě nebo servisních triggerů. Její role je nepostradatelná pro udržení kontinuity relace a umožnění bohatých zážitků s více zařízeními bez nutnosti, aby vzdálená strana znovu navazovala hovor, čímž poskytuje bezproblémový uživatelský zážitek napříč IMS ekosystémem.

## K čemu slouží

Funkce S/C byla vytvořena, aby vyřešila zásadní problém kontinuity relace a média ve světě plně IP, s více přístupy a více zařízeními, který přinesl IMS. Před IMS nabízela telefonie v okruhově komutovaných sítích jednoduché přesměrování hovoru, ale postrádala flexibilitu pro dynamické rozdělování nebo spojování média napříč různými zařízeními a sítěmi v rámci aktivní relace. Jak uživatelé začali vlastnit více komunikačních zařízení (telefon, tablet, laptop) a připojovat se přes různé přístupové technologie (LTE, Wi-Fi, pevný broadband), vznikla potřeba síťového řízení pro správu mediálních toků pro jednu identitu účastníka napříč těmito koncovými body.

Klíčové problémy, které řeší, zahrnují umožnění služeb jako Voice Call Continuity (VCC) a Single Radio Voice Call Continuity (SRVCC), kde musí být hlasový hovor převeden bezproblémově mezi okruhově komutovanou a IMS doménou bez přerušení. Funkce S/C v IMS doméně dokáže během předání spojit mediální cestu. Dále umožňuje inovativní služby jako Simultaneous Ringing, kdy příchozí hovor zazvoní na více zařízeních a uživatel jej může přijmout na kterémkoli z nich. Také podporuje scénáře s více zařízeními pro jednu relaci, jako je použití jednoho zařízení pro audio a druhého pro video. Bez S/C by každé zařízení vyžadovalo samostatný SIP dialog se vzdálenou stranou, což by komplikovalo fakturaci, signalizaci a uživatelský zážitek.

Její vývoj byl motivován snahou učinit komunikační služby uživatelsky orientovanými spíše než zaměřenými na zařízení. S/C abstrahuje složitost více koncových bodů jak pro uživatele, tak pro vzdálenou stranu, což umožňuje síti inteligentně spravovat distribuci média. To podporuje obchodní modely poskytovatelů služeb pro nabídku prémiových služeb kontinuity a služeb pro více zařízení. Standardizací této funkce v 3GPP bylo zajištěno interoperabilita mezi IMS jádry a aplikačními servery různých výrobců, což bylo klíčové pro rozšířené nasazení pokročilých telefonních služeb založených na IMS nahrazujících tradiční okruhově komutované sítě.

## Klíčové vlastnosti

- Rozděluje jeden mediální proud pro doručení na více uživatelských zařízení (např. Simultaneous Ringing)
- Spojuje více příchozích mediálních proudů do jednoho odchozího proudu (např. pro kontinuitu relace)
- Implementována jako IMS Application Server nebo v rámci Media Resource Function (MRF)
- Funguje jako Back-to-Back User Agent (B2BUA) pro řízení mediální cesty
- Využívá SDP offer/answer k navázání více mediálních větví pro jednu relaci
- Umožňuje kontinuitu služeb mezi CS a IMS doménami (např. SRVCC)

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.202** (Rel-19) — CS Bearer Services Architecture in UMTS
- **TR 23.910** (Rel-5) — UMTS Circuit Switched Bearer Services Overview

---

📖 **Anglický originál a plná specifikace:** [S/C na 3GPP Explorer](https://3gpp-explorer.com/glossary/s-c/)
