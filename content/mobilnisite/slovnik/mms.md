---
slug: "mms"
url: "/mobilnisite/slovnik/mms/"
type: "slovnik"
title: "MMS – Multimedia Messaging Service"
date: 2025-01-01
abbr: "MMS"
fullName: "Multimedia Messaging Service"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mms/"
summary: "Standardizovaná služba zasílání zpráv, která umožňuje odesílání a přijímání multimediálních zpráv obsahujících text, obrázky, video a audio mezi mobilními zařízeními. Funguje přes mobilní sítě s využi"
---

MMS je standardizovaná služba zasílání zpráv v mobilních sítích, která využívá mechanismus uložení a přeposlání (store-and-forward) k odesílání a přijímání multimediálních zpráv obsahujících text, obrázky, video a audio mezi mobilními zařízeními.

## Popis

Multimedia Messaging Service (MMS) je služba zasílání zpráv typu uložení a přeposlání (store-and-forward), standardizovaná organizací 3GPP, která umožňuje mobilním účastníkům odesílat a přijímat zprávy obsahující multimediální obsah, jako je formátovaný text, fotografie, audio klipy a video klipy. Na rozdíl od SMS, která je omezena na prostý text, MMS využívá architekturu klient-server, kde zařízení uživatele (MMS User Agent) komunikuje se síťovými servery. Mezi klíčové síťové prvky patří MMSC (Multimedia Messaging Service Centre), který funguje jako centrální uzel pro zpracování zpráv. MMSC se skládá z MMS Relay, která zajišťuje směrování a přenos zpráv mezi různými sítěmi a uživatelskými agenty, a MMS Serveru, který poskytuje úložné kapacity pro zprávy (např. když je příjemce nedostupný) a rozhraní k externím systémům, jako jsou emailové servery.

Technická operace zahrnuje několik fází. Když uživatel odešle MMS zprávu, User Agent odešle zprávu, zakódovanou v multimediálním formátu jako je SMIL (Synchronized Multimedia Integration Language) pro prezentaci, k MMS Relay/Serveru přes referenční bod MM1, typicky s využitím protokolů WAP nebo [HTTP](/mobilnisite/slovnik/http/). MMSC následně zprávu zpracuje, což může zahrnovat překódování mediálních formátů pro kompatibilitu se zařízením příjemce, určení směrování na základě adresy příjemce a komunikaci s jinými systémy zasílání zpráv (např. přes MM3 pro email nebo MM4 pro výměnu MMS mezi operátory). Pro doručení, pokud je příjemce v jiné síti, MMSC použije rozhraní MM4 k přeposlání zprávy do domovského MMSC příjemce, který ji následně doručí do zařízení příjemce přes rozhraní MM1, často s využitím mechanismu push notifikace jako je WAP Push, aby upozornil zařízení na potřebu zprávu stáhnout.

MMS také integruje s podsystémy jádra sítě. Komunikuje s Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) přes referenční bod MM5 za účelem získání dat o účastníkovi a informací pro směrování. Fakturace a účtování jsou usnadněny interakcemi s účtovacími systémy (např. přes MM8). Služba podporuje různé typy obsahu definované [MIME](/mobilnisite/slovnik/mime/) typy a vyžaduje podporu jak v zařízení, tak v síti, což z ní činí složitější službu než SMS, ale která umožnila bohatou multimediální komunikaci v éře před chytrými telefony a v počátcích mobilních dat.

## K čemu slouží

MMS byla vytvořena za účelem rozšíření možností mimořádně úspěšné služby Short Message Service (SMS) za hranice prostého textu a umožnění bohaté multimediální komunikace přes mobilní sítě. Před zavedením MMS nebylo odesílání obrázku nebo zvukového klipu z jednoho telefonu na druhý standardizovanou službou a často se spoléhalo na proprietární řešení nebo email, která nebyla bezproblémově integrována do mobilního uživatelského prostředí. Motivací bylo podpořit adopci mobilních datových služeb ([GPRS](/mobilnisite/slovnik/gprs/), později 3G) poskytnutím atraktivní, uživatelsky přívětivé aplikace, která demonstrovala hodnotu vyšší přenosové kapacity.

Služba řešila omezení formátu SMS pouze na text o délce 160 znaků a umožnila expresivnější komunikaci. Poskytla také standardizovaný, interoperabilní rámec, který zajišťoval, že zprávy mohou být vyměňovány mezi účastníky na sítích různých mobilních operátorů po celém světě, což byl klíčový faktor pro její široké přijetí. Použitím architektury uložení a přeposlání mohlo MMS garantovat doručení zprávy, i když byl telefon příjemce vypnutý nebo mimo dosah signálu, a zprávu uložit na serveru, dokud nemohla být doručena. To z ní učinilo spolehlivou službu, která dobře odpovídala vzorcům používání mobilních sítí v dané době.

## Klíčové vlastnosti

- Architektura uložení a přeposlání (store-and-forward) s centrálním MMSC (Relay/Server)
- Podpora multimediálního obsahu (text, obrázek, audio, video) s využitím MIME typů
- Standardizovaná rozhraní (MM1-MM8) pro interoperabilitu mezi zařízeními a sítěmi
- Integrace s databázemi účastníků (HLR/HSS) pro směrování a autorizaci služby
- Spolupráce s externími systémy zasílání zpráv, jako je email (SMTP) a SMS
- Podpora notifikace o zprávě (např. WAP Push) a její stažení zařízením příjemce

## Definující specifikace

- **TS 22.140** (Rel-19) — MMS Stage 1 Requirements
- **TS 22.233** (Rel-19) — Packet-switched Streaming Service (PSS) Stage 1
- **TS 22.242** (Rel-19) — DRM Service Requirements
- **TR 22.940** (Rel-19) — IMS Messaging Requirements Analysis
- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TS 24.447** (Rel-8) — Advice Of Charge (AOC) Service Protocol
- **TS 24.526** (Rel-19) — UE Policies for 5GS; Stage 3
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 26.140** (Rel-19) — MMS Media Formats and Codecs Specification
- **TS 26.141** (Rel-19) — IMS Messaging & Presence Media Formats
- **TS 26.142** (Rel-19) — 3GPP TS 26.142: Dynamic and Interactive Multimedia Scenes (DIMS)
- **TS 26.143** (Rel-19) — 5G Messaging Media Types and Codecs
- **TS 26.233** (Rel-15) — 3GPP Packet-Switched Streaming Service (PSS)
- … a dalších 36 specifikací

---

📖 **Anglický originál a plná specifikace:** [MMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/mms/)
