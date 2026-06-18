---
slug: "vbd"
url: "/mobilnisite/slovnik/vbd/"
type: "slovnik"
title: "VBD – VoiceBand Data"
date: 2025-01-01
abbr: "VBD"
fullName: "VoiceBand Data"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/vbd/"
summary: "VoiceBand Data (VBD) označuje přenos datových signálů, jako je fax nebo modemová komunikace, přes hlasový kanál v rámci přepojování okruhů nebo paketů v telefonní síti. Je definováno v mnoha specifika"
---

VBD je přenos datových signálů, jako je fax nebo modemová komunikace, přes hlasový kanál, aby bylo možné provozovat starší datové služby na moderních IP sítích, jako jsou LTE a 5G.

## Popis

VoiceBand Data (VBD) je služba, která umožňuje přenos nehlasových datových signálů – konkrétně těch generovaných analogovými modemy, faxovými přístroji skupiny 3 nebo textovými telefony – přes telefonní síť tím, že je zachází jako s audio signálem v hlasovém frekvenčním pásmu (typicky 300–3400 Hz). V architekturách 3GPP, zejména od Release 8 s IP Multimedia Subsystem (IMS), je VBD implementováno prostřednictvím mediálních bran a propojovacích funkcí, které zajišťují konverzi mezi tradičními daty s přepojováním okruhů a přenosy VoIP s přepojováním paketů. Když je VBD hovor navázán (např. faxový hovor), koncové zařízení (UE) nebo síťová brána detekuje tóny datového modemu a klasifikuje relaci jako VBD namísto běžného hlasu. Jádrová síť, využívající Media Gateway Control Function ([MGCF](/mobilnisite/slovnik/mgcf/)) a Media Gateway ([MGW](/mobilnisite/slovnik/mgw/)) podle TS 29.332, zajišťuje, že přenosová cesta je nakonfigurována tak, aby podporovala transparentní přenos dat bez hlasové komprese, potlačení ozvěn nebo jiného hlasově optimalizovaného zpracování, které by mohlo poškodit datové signály. V kontextu IMS může Telephony Application Server ([TAS](/mobilnisite/slovnik/tas/)) nebo specializovaný VBD aplikační server řídit relaci a používat specifické kodeky jako G.711 (který poskytuje nekomprimované [PCM](/mobilnisite/slovnik/pcm/) audio), aby byla zachována integrita modulovaných dat. Data jsou paketizována pomocí [RTP](/mobilnisite/slovnik/rtp/) přes IP a směrována přes IMS core k cílovému koncovému bodu, kterým může být další VBD-kompatibilní terminál nebo brána do [PSTN](/mobilnisite/slovnik/pstn/). Tento end-to-end proces umožňuje bezproblémový provoz starších datových služeb na plně IP sítích, jako jsou LTE a 5G, při zachování interoperability bez nutnosti změn na faxových přístrojích nebo modemech koncového uživatele.

## K čemu slouží

VoiceBand Data bylo vyvinuto, aby řešilo kritickou potřebu zpětné kompatibility při přechodu telekomunikačních sítí z technologií s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)), jako jsou GSM a UMTS, na plně IP architektury s přepojováním paketů, jako jsou LTE a 5G. Tradiční datové služby, jako je fax a vytáčený přístup k internetu, spoléhají na analogové modemové signály přenášené přes hlasové kanály, které byly nativně podporovány v CS sítích, ale nejsou přímo kompatibilní s VoIP systémy používajícími kompresi a optimalizaci hlasu. Bez VBD by tyto nezbytné služby v moderních sítích selhaly, což by narušilo obchodní, lékařskou a právní komunikaci, která stále závisí na faxu. Tato technologie tento problém řeší tím, že zajistí, aby síť dokázala tyto datové hovory identifikovat a speciálně zpracovat, a obchází tak škodlivé hlasové zpracování. Jeho specifikace napříč více releasy 3GPP (počínaje IMS v Rel-8) poskytla standardizované propojovací řešení, které umožnilo operátorům vyřadit starší CS infrastrukturu při zachování kontinuity služeb. VBD tak překlenuje propast mezi starými a novými síťovými technologiemi a podporuje hladkou migraci na IP-based core.

## Klíčové vlastnosti

- Detekce a klasifikace modemových/faxových tónů pro aktivaci VBD režimu
- Použití transparentních, nekomprimovaných kodeků (např. G.711) pro zachování integrity datového signálu
- Obcházení hlasově optimalizačního zpracování, jako je potlačení ozvěn a detekce hlasové aktivity
- Propojení mezi paketově přepínaným IMS a sítěmi s přepojováním okruhů prostřednictvím mediálních bran
- Podpora jak protokolů pro fax v reálném čase (T.38), tak modemových relay protokolů jako záložních řešení
- Řízení relace prostřednictvím IMS aplikačních serverů a MGCF pro správné směrování

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)

## Definující specifikace

- **TS 29.332** (Rel-19) — MGCF-IM-MGW Interface Protocol (Mn)
- **TS 29.333** (Rel-19) — MRFC-MRFP Mp Interface Protocol
- **TS 29.412** (Rel-8) — Trunking Gateway Control Procedures
- **TS 29.424** (Rel-8) — H.248 Profile for Trunking Media Gateways

---

📖 **Anglický originál a plná specifikace:** [VBD na 3GPP Explorer](https://3gpp-explorer.com/glossary/vbd/)
