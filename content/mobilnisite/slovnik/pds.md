---
slug: "pds"
url: "/mobilnisite/slovnik/pds/"
type: "slovnik"
title: "PDS – Packet Data Subsystem"
date: 2025-01-01
abbr: "PDS"
fullName: "Packet Data Subsystem"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pds/"
summary: "Packet Data Subsystem (PDS) je komponenta architektury jádra sítě definovaná pro služby IP Multimedia Subsystem (IMS). Poskytuje rámec pro paketově přepínané datové služby, včetně řízení relací, vynuc"
---

PDS je komponenta architektury jádra sítě pro služby IMS, která poskytuje rámec pro paketově přepínané datové služby, včetně řízení relací a vynucování pravidel, a umožňuje multimédia přes LTE a 5G.

## Popis

Packet Data Subsystem (PDS) je koncept funkční architektury definovaný ve specifikacích 3GPP, primárně v kontextu IP Multimedia Subsystem (IMS). Představuje soubor síťových entit a funkcí zodpovědných za poskytování paketově přepínaných datových služeb. PDS není jediný fyzický uzel, ale logické seskupení zahrnující prvky podílející se na správě relací, řízení přenosových kanálů, vynucování pravidel a tarifování a přenosu uživatelských dat. Jeho definice pomáhá strukturovat síť pro doručování multimediálních služeb přes plně IP sítě.

Architektonicky PDS rozhraní s jádrem IMS pro řízení služeb a s rádiovou přístupovou sítí (RAN) pro konektivitu uživatelské roviny. Zahrnuje funkce jako Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)), Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) v LTE a User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v 5G. Tyto komponenty spolupracují na vytváření, udržování a ukončování datových relací, aplikaci pravidel kvality služeb (QoS) a správě tarifování na základě využití služeb. PDS zajišťuje správné směrování datových paketů mezi uživatelským zařízením a externími paketovými datovými sítěmi.

Role PDS je ústřední pro provoz moderního mobilního širokopásmového připojení. Odděluje řídicí rovinu (zpracovávanou IMS a [MME](/mobilnisite/slovnik/mme/)/[AMF](/mobilnisite/slovnik/amf/)) od uživatelské roviny, což umožňuje škálovatelný a efektivní datový přenos. Definicí tohoto subsystému poskytuje 3GPP jasný model pro implementaci a propojení různých síťových funkcí potřebných pro paketové datové služby, což usnadňuje interoperabilitu mezi dodavateli a konzistentní poskytování služeb napříč různými generacemi mobilních sítí.

## K čemu slouží

Packet Data Subsystem byl vytvořen, aby poskytl standardizovaný architektonický rámec pro doručování paketově přepínaných datových služeb v sítích 3GPP, zejména když služby překročily rámec tradičního okruhově přepínaného hlasu. Před jeho definicí byly možnosti paketových dat roztříštěnější, přičemž funkce jako [GPRS](/mobilnisite/slovnik/gprs/) podpůrné uzly (GGSN, [SGSN](/mobilnisite/slovnik/sgsn/)) poskytovaly datové služby, ale bez jednotného modelu subsystému integrovaného s IMS pro multimédia. Vzestup IMS a potřeba bohatých multimediálních služeb (hlas přes IP, videohovory, zasílání zpráv) přes LTE si vyžádaly koherentní architekturu, která by dokázala integrovaně zvládat řízení relací, pravidla a tarifování.

PDS řeší problém, jak efektivně spravovat a doručovat služby založené na IP, seskupením příbuzných funkcí pro paketová data. Řeší výzvu zajištění konzistentní QoS, zabezpečení a tarifování pro různé služby od různých poskytovatelů. Definicí tohoto subsystému umožnilo 3GPP operátorům systematickyji nasazovat a spravovat paketové datové služby, podporovat přechod na plně IP sítě a položit základy pro architektury založené na službách používané v 5G. Jeho vytvoření bylo motivováno pohybem průmyslu směrem ke konvergenci pevných a mobilních sítí a doručování bezproblémových multimediálních zážitků.

## Klíčové vlastnosti

- Poskytuje architektonický rámec pro paketově přepínané datové služby
- Integruje se s IMS pro řízení multimediálních relací
- Zahrnuje funkce vynucování pravidel a tarifování
- Spravuje konektivitu uživatelské roviny a směrování dat
- Podporuje diferenciaci kvality služeb (QoS) pro jednotlivé služby
- Usnadňuje interoperabilitu mezi funkcemi jádra sítě

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [PGW – PDN Gateway](/mobilnisite/slovnik/pgw/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [EPS – Evolved Packet System](/mobilnisite/slovnik/eps/)

## Definující specifikace

- **TS 23.167** (Rel-19) — IMS Emergency Sessions

---

📖 **Anglický originál a plná specifikace:** [PDS na 3GPP Explorer](https://3gpp-explorer.com/glossary/pds/)
