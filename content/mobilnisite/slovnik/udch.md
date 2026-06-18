---
slug: "udch"
url: "/mobilnisite/slovnik/udch/"
type: "slovnik"
title: "UDCH – User-plane Dedicated CHannel"
date: 2025-01-01
abbr: "UDCH"
fullName: "User-plane Dedicated CHannel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/udch/"
summary: "Vyhrazený transportní kanál v systémech GSM a UMTS používaný pro přenos uživatelských dat (např. hlasu nebo paketových dat) pro konkrétní spojení. Poskytuje garantované, okruhově přepínaným připojením"
---

UDCH je vyhrazený transportní kanál v GSM a UMTS, který poskytuje garantované, okruhově přepínaným připojením podobné prostředky pro přenos uživatelských dat pro konkrétní spojení a zajišťuje konzistentní kvalitu služeb.

## Popis

Uživatelský vyhrazený kanál (User-plane Dedicated CHannel – UDCH) je základní koncept transportního kanálu v rádiových přístupových sítích 2G GSM a 3G UMTS. Jedná se o vyhrazený bod-bod kanál zřízený mezi jedním uživatelským zařízením (UE) a sítí ([BSS](/mobilnisite/slovnik/bss/) v GSM, [UTRAN](/mobilnisite/slovnik/utran/) v UMTS) výhradně pro přenos uživatelských dat. Na rozdíl od společných kanálů sdílených mnoha uživateli přiděluje UDCH konkrétní rádiové prostředky (časové sloty v GSM, kód/výkon v UMTS) pro výhradní použití jednoho spojení, což poskytuje předvídatelný výkon. V GSM je typicky realizován jako kanál pro přenos hovoru ([TCH](/mobilnisite/slovnik/tch/)), zatímco v UMTS odpovídá na úrovni transportního kanálu vyhrazenému kanálu ([DCH](/mobilnisite/slovnik/dch/)).

Z architektonického hlediska je UDCH zřizován a spravován protokolem řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)). Pro hlasový hovor síť přiřadí UDCH s pevnou přenosovou rychlostí (např. 12,2 kbps pro hlas [AMR](/mobilnisite/slovnik/amr/)). Pro paketově přepínaná data může být UDCH zřízen s konkrétní přenosovou rychlostí po dobu aktivního přenosu dat. Parametry fyzické vrstvy kanálu (jako rozprostírací kód v UMTS) konfiguruje [RNC](/mobilnisite/slovnik/rnc/)/[BSC](/mobilnisite/slovnik/bsc/). Uživatelská data z vyšších vrstev (např. hlasové rámce nebo IP pakety) jsou zpracována protokolovým zásobníkem (RLC, MAC) a následně namapována na tento vyhrazený transportní kanál pro přenos přes rozhraní vzduch.

Jeho úlohou je poskytovat řízenou, vysoce spolehlivou cestu pro uživatelská data se zaručenými parametry kvality služeb (QoS), jako je přenosová rychlost a zpoždění. To je nezbytné pro okruhově přepínané služby, jako je hlas a videotelefonie, a bylo také využíváno pro rané vysokorychlostní paketové datové služby (jako HSDPA, které zpočátku používaly sdílený kanál pro downlink, ale často DCH/UDCH pro uplink). Správa UDCH je klíčovou funkcí RAN a zahrnuje řízení přístupu, řízení výkonu a procedury předávání hovoru, aby byla zachována kvalita kanálu při pohybu uživatele.

## K čemu slouží

UDCH byl vyvinut pro podporu spolehlivých služeb komunikace v reálném čase v digitálních celulárních sítích. V rané éře GSM byla primární službou okruhově přepínaný hlas, který vyžadoval vyhrazené, nepřetržité spojení s minimálním zpožděním a chvěním. UDCH (jako TCH) to poskytoval napodobováním fyzického okruhu přes rádiové rozhraní a garantováním prostředků po dobu trvání hovoru.

S vývojem směrem k UMTS a paketově přepínaným datům zůstal tento koncept klíčový pro služby vyžadující konzistentní QoS. Zatímco sdílené kanály jsou efektivnější pro trhavá data, aplikace jako videohovory nebo interaktivní hraní potřebovaly předvídatelný výkon vyhrazeného kanálu. UDCH vyřešil problém, jak poskytovat řízené, spojením orientované služby přes paketově orientovanou rádiovou přístupovou síť. Umožnil síti provádět přesné řízení rádiových prostředků, řízení výkonu a měkké předávání hovoru, čímž zajišťoval kontinuitu a kvalitu služby. Jeho vytvoření bylo motivováno potřebou rozšířit kvalitativní záruky okruhově přepínaného hlasu na vznikající multimediální služby.

## Klíčové vlastnosti

- Bod-bod vyhrazený transportní kanál pro jedno uživatelské zařízení (UE)
- Poskytuje garantovanou přenosovou rychlost a QoS po dobu trvání spojení
- Spravován pomocí signalizace RRC pro zřízení, rekonfiguraci a uvolnění
- Mapuje uživatelská data (hlas, video, pakety) z vrstev RLC/MAC
- Nezbytný pro okruhově přepínané služby a QoS-aware paketová data
- Zahrnuje řízení přístupu, řízení výkonu a předávání hovoru řízené sítí

## Související pojmy

- [DCH – Dedicated Channel](/mobilnisite/slovnik/dch/)
- [TCH – Traffic Channel](/mobilnisite/slovnik/tch/)
- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification
- **TR 45.902** (Rel-19) — Flexible Layer One (FLO) for GERAN

---

📖 **Anglický originál a plná specifikace:** [UDCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/udch/)
