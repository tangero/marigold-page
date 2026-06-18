---
slug: "vxml"
url: "/mobilnisite/slovnik/vxml/"
type: "slovnik"
title: "VXML – Voice Extensible Markup Language"
date: 2025-01-01
abbr: "VXML"
fullName: "Voice Extensible Markup Language"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/vxml/"
summary: "Značkovací jazyk založený na XML pro vytváření interaktivních hlasových odpovědí (IVR) a hlasem řízených telekomunikačních aplikací. V rámci 3GPP je standardizován pro vývoj služeb v IP Multimedia Sub"
---

VXML je značkovací jazyk založený na XML, standardizovaný konsorciem 3GPP, pro vytváření hlasem řízených aplikací (např. IVR) v IMS, který odděluje aplikační logiku od zpracování médií pro webově podobné nasazení.

## Popis

Voice Extensible Markup Language (VXML), standardizovaný konsorciem [W3C](/mobilnisite/slovnik/w3c/) a přijatý konsorciem 3GPP ve specifikaci 23.333, je klíčovou technologií pro vývoj hlasových služeb v telekomunikačních sítích, zejména v rámci IP Multimedia Subsystem (IMS). Funguje jako aplikační protokol, který definuje průběh dialogu mezi uživatelem a hlasovou službou. Dokument (neboli skript) VXML je zpracováván speciálním interpretem nazývaným Hlasový prohlížeč (Voice Browser), který běží na mediálním serveru (např. Media Resource Function Processor, [MRFP](/mobilnisite/slovnik/mrfp/)). Tento prohlížeč skript vykonává, řídí přehrávání zvuku (syntetizovaná řeč nebo předem nahrané audio), zpracovává vstup od uživatele (řeč nebo [DTMF](/mobilnisite/slovnik/dtmf/) tóny) a rozhoduje o logice navigace během hovoru.

Architektura zahrnuje několik klíčových komponent. Architektura VXML Fóra, na kterou 3GPP odkazuje, zahrnuje Hlasový prohlížeč, který načítá VXML dokumenty z aplikačního serveru ([AS](/mobilnisite/slovnik/as/)) prostřednictvím [HTTP](/mobilnisite/slovnik/http/). Aplikační server hostuje servisní logiku a obchodní pravidla a generuje dynamické VXML stránky. Mediální server poskytuje vlastní zdroje pro rozpoznávání řeči ([ASR](/mobilnisite/slovnik/asr/)), syntézu řeči ([TTS](/mobilnisite/slovnik/tts/)) a přehrávání audia. Skript VXML se skládá z řady dialogových stavů (jako <form> a <menu>) obsahujících elementy <field> pro sběr vstupu, elementy <prompt> pro přehrávání audia a bloky <filled>, které definují akce provedené po přijetí vstupu. Zpracování událostí (<catch>) řeší chyby a neočekávané vstupy. Tento deklarativní model odděluje servisní logiku na AS od detailů zpracování médií, což vývojářům umožňuje soustředit se na konverzační design.

V síti IMS dle 3GPP hraje VXML klíčovou roli při umožňování standardizovaných, na síti nezávislých hlasových aplikací. Když účastník IMS zahájí hlasový hovor ke službě (např. hlasový portál, automatická zákaznická podpora nebo konferenční systém), Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) směruje hovor na příslušný aplikační server na základě počátečních filtračních kritérií (iFC). Tento AS pak může fungovat jako interpret VXML nebo, častěji, načítat VXML dokumenty z webového serveru a předávat je specializované Media Resource Function (MRF), která hostuje Hlasový prohlížeč. MRF naváže s uživatelským zařízením mediální relaci pomocí protokolů jako RTP a provede VXML dialog. To umožňuje bohaté, interaktivní služby, jako je hlasové vytáčení, hlasové zprávy, ovládání audiokonferencí a hlasové portály s přirozeným jazykem, které jsou všechny poskytovány plynule přes paketové sítě IMS spolu s dalšími multimediálními službami.

## K čemu slouží

VXML byl vytvořen, aby vyřešil historický problém proprietárního, složitého a nákladného vývoje systémů interaktivních hlasových odpovědí (IVR). Před VXML se IVR aplikace typicky stavěly pomocí nízkoúrovňových, na dodavateli závislých programovacích jazyků a nástrojů, které těsně svazovaly aplikační logiku s telekomunikačním hardwarem a mediálními zdroji. To činilo aplikace obtížně přenositelnými, nákladnými na vývoj a údržbu a omezovalo inovace na malou skupinu specializovaných vývojářů.

Přijetí VXML konsorciem 3GPP, počínaje Release 7, bylo motivováno přechodem na plně IP sítě a IMS. IMS měl za cíl poskytnout standardizované prostředí pro tvorbu multimediálních služeb. Pro hlasové služby bylo potřeba modelu inspirovaného webem. VXML přesně toto poskytl: aplikoval úspěšný paradigma webového vývoje (klient-server, značkovací jazyky, HTTP) na svět hlasu. Použitím XML se stalo snadným generovat dynamické hlasové dialogy z webových aplikačních serverů, což umožnilo široké komunitě webových vývojářů vytvářet telekomunikační aplikace. Tím byly odstraněny limity starého přístupu podporou interoperability, snížením doby vývoje, podporou ekosystému nástrojů a umožněním snadné integrace hlasových služeb s webovými daty a obchodní logikou. Byl to klíčový faktor pro poskytování konzistentních, pokročilých hlasových služeb napříč vyvíjející se síťovou krajinou směrem k LTE a 5G.

## Klíčové vlastnosti

- Deklarativní jazyk založený na XML pro definici hlasových dialogů a průběhů hovorů
- Oddělení servisní logiky (na aplikačním serveru) od zpracování médií (na mediálním serveru)
- Podpora integrace rozpoznávání řeči (ASR) a syntézy řeči (TTS)
- Architektura řízená událostmi s obslužnými rutinami pro chyby, nedostatek vstupu a neshodu
- Schopnost dynamicky načítat a vykonávat skripty prostřednictvím HTTP z webových serverů
- Podpora vstupu DTMF, přehrávání zvukových souborů a odesílání proměnných dat (HTTP POST)

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MRF – Multimedia Resource Function](/mobilnisite/slovnik/mrf/)
- [IVR – Interactive Voice Response](/mobilnisite/slovnik/ivr/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [RTP – Real-time Transport Protocol](/mobilnisite/slovnik/rtp/)

## Definující specifikace

- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements

---

📖 **Anglický originál a plná specifikace:** [VXML na 3GPP Explorer](https://3gpp-explorer.com/glossary/vxml/)
