---
slug: "o-mgcf"
url: "/mobilnisite/slovnik/o-mgcf/"
type: "slovnik"
title: "O-MGCF – Outgoing - Media Gateway Control Function"
date: 2025-01-01
abbr: "O-MGCF"
fullName: "Outgoing - Media Gateway Control Function"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/o-mgcf/"
summary: "Funkční role MGCF, když řídí Media Gateway (MGW) pro účast hovoru, která opouští IMS síť směrem k přepojované síti, jako je PSTN nebo starší PLMN. Provádí protokolovou interoperabilitu mezi SIP (IMS)"
---

O-MGCF je funkční role Media Gateway Control Function, když řídí Media Gateway pro účast hovoru opouštějící IMS síť směrem k přepojované síti a provádí protokolovou interoperabilitu mezi SIP a ISUP/BICC.

## Popis

O-MGCF není samostatný síťový prvek, ale specifická provozní role nebo perspektiva Media Gateway Control Function ([MGCF](/mobilnisite/slovnik/mgcf/)) v rámci architektury IMS podle 3GPP. MGCF je centrální řídicí jednotka odpovědná za relace vyžadující interoperabilitu mezi IP doménou IMS a externími přepojovanými ([CS](/mobilnisite/slovnik/cs/)) sítěmi, jako je veřejná telefonní síť ([PSTN](/mobilnisite/slovnik/pstn/)) nebo starší jádro GSM/UMTS CS. Označení 'Outgoing' (odchozí) se vztahuje k funkci MGCF, když zpracovává účast hovoru, která vzniká uvnitř IMS a směřuje ven do CS sítě. V této roli O-MGCF vystupuje jako [SIP](/mobilnisite/slovnik/sip/) User Agent Client ([UAC](/mobilnisite/slovnik/uac/)) pro odchozí účast.

Když uživatel IMS iniciuje hovor na číslo v PSTN, [S-CSCF](/mobilnisite/slovnik/s-cscf/) směruje SIP INVITE na MGCF na základě analýzy cíle. MGCF, přebírající roli O-MGCF, provádí několik klíčových funkcí. Za prvé provádí mapování a překlad protokolů mezi signalizací SIP z IMS a signalizací [ISUP](/mobilnisite/slovnik/isup/) ([ISDN](/mobilnisite/slovnik/isdn/) User Part) nebo BICC (Bearer Independent Call Control) používanou v CS síti. To zahrnuje překlad SIP metod, hlaviček a nabídek/odpovědí SDP (Session Description Protocol) do ekvivalentních zpráv a informací o nosiči ISUP/BICC. Za druhé O-MGCF řídí jeden nebo více Media Gateway (MGW) pomocí protokolu H.248 (Megaco). Přikazuje MGW, aby zřídil potřebná spojení nosiče, včetně transkódování kodeků mezi kodeky IMS (např. AMR, EVS) a kodeky CS (např. G.711), a aby propojil IP nosič z IMS s TDM nebo IP nosičem vedoucím do CS sítě.

Z architektonického hlediska O-MGCF komunikuje s jádrem IMS přes rozhraní Mg (SIP), s CS sítí přes rozhraní Nb (pomocí ISUP/BICC přes MTP3/SCTP/IP) a s MGW přes rozhraní Mn (H.248). Jeho role je klíčová pro bezproblémovou kontinuitu služeb, umožňující účastníkům IMS komunikovat s uživateli na jakékoli starší telefonní síti. Doplňkovou rolí je T-MGCF (Terminating MGCF), která zpracovává hovory vstupující do IMS z CS sítě. O-MGCF zajišťuje, že řízení hovoru, fakturační informace a doplňkové služby jsou správně přeloženy a zachovány přes hranici sítě.

## K čemu slouží

Role O-MGCF byla formálně definována, aby objasnila funkce řízení hovoru MGCF v dekomponované architektuře sítě nové generace, zejména s dozráváním IMS v 3GPP Release 7 a novějších. Starší verze představily MGCF, ale rozlišení mezi jejím odchozím a koncovým chováním získalo na důležitosti s plnou dekompozicí MSC na MSC Server a MGW a s potřebou přesných scénářů interoperability. Účelem definice O-MGCF je specifikovat přesné postupy, mapování protokolů a správu stavu vyžadované při přechodu relace iniciované z IMS do světa starší telefonie.

Řeší kritický problém protokolové a servisní interoperability mezi relacemi orientovaným, textovým protokolem SIP v IMS a spojení orientovanou, zprávami založenou signalizací (ISUP/BICC) přepojovaných sítí. Bez překladových funkcí O-MGCF by byly sítě IMS izolovanými ostrovy. O-MGCF umožňuje operátorům nasadit IMS jako síť jádra při zachování plné konektivity ke globální PSTN, čímž chrání stávající investice a zajišťuje univerzální službu. Jeho vznik byl motivován praktickou nutností postupné migrace sítě, kde musí IMS a starší sítě koexistovat po mnoho let, a potřebou standardizovaného, mezi dodavateli interoperabilního způsobu zpracování složitého překladu signalizace pro odchozí hovory, včetně podpory základních telefonních funkcí, jako je identifikace volajícího, přesměrování hovoru a vyjednávání řečového kodeku.

## Klíčové vlastnosti

- Definuje roli MGCF pro účasti hovoru z IMS do CS sítě
- Provádí protokolovou interoperabilitu mezi SIP a ISUP/BICC
- Řídí Media Gateway pomocí protokolu H.248 (Megaco)
- Spravuje zřizování prostředků nosiče a transkódování kodeků
- Vystupuje jako SIP User Agent Client (UAC) pro odchozí účast
- Překládá parametry relace IMS na informace o nosiči CS sítě

## Související pojmy

- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)
- [MGW – Media Gateway](/mobilnisite/slovnik/mgw/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [PSTN – Public Switched Telecommunications Network](/mobilnisite/slovnik/pstn/)

## Definující specifikace

- **TS 24.411** (Rel-8) — ACR and CB Service Protocol Specification
- **TS 24.428** (Rel-7) — Common Basic Communication Procedures
- **TS 24.504** (Rel-8) — Communication Diversion Services Stage 3
- **TS 24.528** (Rel-8) — Common Basic Communication Procedures for IMS Services
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks

---

📖 **Anglický originál a plná specifikace:** [O-MGCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/o-mgcf/)
