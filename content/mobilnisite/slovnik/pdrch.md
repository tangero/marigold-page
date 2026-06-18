---
slug: "pdrch"
url: "/mobilnisite/slovnik/pdrch/"
type: "slovnik"
title: "PDRCH – Physical Device-to-Reader Channel"
date: 2026-01-01
abbr: "PDRCH"
fullName: "Physical Device-to-Reader Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pdrch/"
summary: "Fyzický kanál mezi zařízením a čtečkou (Physical Device-to-Reader Channel, PDRCH) je vyhrazený fyzický kanál zavedený ve specifikaci 3GPP Release 19 pro přímou komunikaci mezi čtecím zařízením a pasiv"
---

PDRCH je vyhrazený fyzický kanál ve specifikaci 3GPP Release 19 pro přímou, efektivní a nízkopříkonovou komunikaci mezi čtecím zařízením a pasivním či semi-pasivním tagem nebo senzorem ve scénářích masivního IoT.

## Popis

Fyzický kanál mezi zařízením a čtečkou (Physical Device-to-Reader Channel, PDRCH) je nová komponenta rozhraní pro přenos vzduchem definovaná ve specifikaci 3GPP Release 19, primárně v kontextu NR-Light (RedCap) a vylepšených pracovních položek pro IoT. Vytváří jednosměrný nebo obousměrný kanál fyzické vrstvy umožňující efektivní komunikaci mezi aktivním zařízením typu 'Čtečka' (kterým může být základnová stanice, dedikovaná čtečka nebo schopné UE) a potenciálně velkým počtem jednoduchých, nízkonákladových 'Zařízení'. Tato zařízení jsou typicky pasivní (založená na principu zpětného rozptylu) nebo semi-pasivní (s bateriovou podporou) tagy nebo senzory, jako jsou například ty používané v [RFID](/mobilnisite/slovnik/rfid/), chytré logistice nebo průmyslovém monitoringu. PDRCH je navržen tak, aby byl extrémně efektivní z hlediska využití zdrojů a minimalizoval energetické nároky a složitost na straně Zařízení.

PDRCH funguje v rámci architektury NR (New Radio) a může být konfigurován v licencovaném spektru (jako část sítě operátora) nebo v nelicencovaném/sdíleném spektru (pro privátní nasazení). Z perspektivy fyzické vrstvy PDRCH definuje specifické průběhy signálu, modulační schémata (často velmi jednoduchá, jako [OOK](/mobilnisite/slovnik/ook/) nebo [BPSK](/mobilnisite/slovnik/bpsk/)) a metody alokace zdrojů (časové/frekvenční bloky), které jsou optimalizovány pro krátké, dávkové přenosy a příjem s vysokou citlivostí. Čtečka vysílá silnou spojitou vlnu ([CW](/mobilnisite/slovnik/cw/)) nebo modulovaný excitační signál, který poskytuje jak energii (pro pasivní zařízení prostřednictvím [RF](/mobilnisite/slovnik/rf/) energy harvestingu), tak i hodinovou referenci. Zařízení odpovídají modulací svých dat na tuto nosnou vlnu pomocí technik zpětného rozptylu nebo vysíláním jednoduchého uplink signálu, vše v rámci předdefinovaných zdrojů PDRCH.

Mezi klíčové architektonické komponenty patří konfigurace PDRCH, která je vysílána sítí nebo Čtečkou a informuje Zařízení o časování, frekvenci a parametrech přístupu. Kanál podporuje víceuživatelské přístupy, potenciálně využívající techniky jako časově dělený ALOHA nebo [FDMA](/mobilnisite/slovnik/fdma/) pro zvládání kolizí při odpovědi mnoha Zařízení. Protokolový stack nad PDRCH je odlehčený a může pro velmi malé datové pakety obcházet vyšší vrstvy protokolů, aby se snížila režie. PDRCH umožňuje dvě primární operace: Inventarizaci, při které Čtečka objevuje a identifikuje všechna Zařízení ve své pokryté oblasti, a Přenos dat, při kterém Čtečka čte data ze nebo zapisuje data do konkrétních Zařízení. Tento kanál je spravován RAN sítě a může být integrován s funkcemi core sítě pro správu zařízení a agregaci dat.

## K čemu slouží

PDRCH byl vytvořen, aby řešil omezení stávajících technologií pro celulární IoT (jako NB-IoT a LTE-M) a necelaulárních [RFID](/mobilnisite/slovnik/rfid/) systémů pro novou generaci masivního měření a identifikace. Zatímco NB-IoT vyniká v připojování senzorů napájených bateriemi, je stále příliš složitý a energeticky náročný pro skutečně pasivní, cenově citlivá zařízení, jako jsou RFID tagy na úrovni jednotlivých položek. Naopak tradiční RFID systémy (např. [UHF](/mobilnisite/slovnik/uhf/) Gen2) fungují v nelicencovaných pásmech s omezeným dosahem, spolehlivostí a bez integrace s celulárními sítěmi široké oblasti pro bezproblémový přenos dat a správu.

PDRCH si klade za cíl tuto mezeru zaplnit definováním standardizovaného, celulární sítí asistovaného kanálu, který kombinuje to nejlepší z obou světů: ultranízkou cenu a nulovou spotřebu pasivního RFID s řízenými, spolehlivými atributy a širokým pokrytím licencované celulární sítě. Tím se řeší problém připojení miliard 'věcí' – od produktů ve skladu po senzory na farmě – které jsou v současnosti offline nebo závisí na proprietárních, izolovaných systémech. Fungováním pod hlavičkou 3GPP umožňuje PDRCH globální škálovatelnost, interoperabilitu a přímou integraci se sítěmi operátorů pro autentizaci, zabezpečení a datové služby.

Dále podporuje nové obchodní modely a případy užití pro operátory, jako je poskytování 'sensing-as-a-service' nebo umožnění vysoce přesného sledování aktivit v širokých oblastech. Použití částí licencovaného spektra může ve srovnání s přeplněnými nelicencovanými ISM pásmy zlepšit spolehlivost a snížit interferenci. Vytvoření PDRCH v Release 19 odráží expanzi 3GPP za tradiční komunikaci zaměřenou na člověka směrem k všudypřítomné komunikaci mezi stroji a tvoří kritický kus roadmapy směrem k vizi skutečně propojeného fyzického světa.

## Klíčové vlastnosti

- Podporuje komunikaci s pasivními (zpětně rozptylujícími) a semi-pasivními zařízeními
- Funguje v licencovaném i nelicencovaném spektru v rámci architektury NR
- Využívá energeticky efektivní průběhy signálu a jednoduchou modulaci (např. OOK, BPSK)
- Umožňuje procedury inventarizace a přenosu dat iniciované Čtečkou
- Navržen pro masivní konektivitu s víceuživatelským přístupem odolným vůči kolizím
- Integrován se sítí 3GPP pro autentizaci, zabezpečení a přenos dat

## Související pojmy

- [RFID – Radio-Frequency Identification](/mobilnisite/slovnik/rfid/)

## Definující specifikace

- **TS 38.191** (Rel-19) — NR Ambient IoT RF Characteristics
- **TS 38.291** (Rel-19) — Ambient IoT Physical Layer Specification
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.391** (Rel-19) — NR; Ambient IoT MAC Protocol Spec
- **TS 38.769** (Rel-20) — Ambient IoT Solutions in NR

---

📖 **Anglický originál a plná specifikace:** [PDRCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/pdrch/)
