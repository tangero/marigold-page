---
slug: "udc"
url: "/mobilnisite/slovnik/udc/"
type: "slovnik"
title: "UDC – Uplink Data Compression"
date: 2026-01-01
abbr: "UDC"
fullName: "Uplink Data Compression"
category: "Radio Access Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/udc/"
summary: "Funkce rádiového rozhraní, která komprimuje uživatelská data ve směru uplink před jejich přenosem vzduchem. Snižuje objem dat odesílaných z UE do sítě, čímž šetří rádiové zdroje, snižuje spotřebu ener"
---

UDC je funkce rádiového rozhraní, která komprimuje uživatelská data ve směru uplink před přenosem, aby snížila objem dat, ušetřila rádiové zdroje, snížila spotřebu energie UE a zlepšila spektrální účinnost.

## Popis

Uplink Data Compression (UDC) je funkce pro zvýšení výkonu v 3GPP LTE a 5G NR, která funguje na vrstvě Packet Data Convergence Protocol ([PDCP](/mobilnisite/slovnik/pdcp/)). Jejím hlavním účelem je aplikace bezztrátových kompresních algoritmů na datové pakety uživatelské roviny ve směru uplink (od uživatelského zařízení k základnové stanici) předtím, než jsou zašifrovány a přeneseny přes rádiové rozhraní. Proces zahrnuje komprimaci IP paketů (včetně hlaviček a datové části) na straně UE a jejich dekomprimaci v přijímacím síťovém uzlu (eNodeB/gNB). Kompresní kontext je vytvořen a synchronizován mezi UE a sítí během nastavení nebo rekonfigurace rádiového beareru.

Z architektonického hlediska je UDC integrováno do PDCP entity pro konkrétní datový rádiový bearer. Při konfiguraci sítí prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/) aplikuje PDCP vrstva UE kompresní algoritmus (např. založený na principech Robust Header Compression ([ROHC](/mobilnisite/slovnik/rohc/)) nebo na vyhrazených algoritmech UDC) na příchozí IP pakety z vyšších vrstev. Komprimovaný paket spolu s potřebnými řídicími informacemi je následně zpracován standardními PDCP funkcemi, jako je šifrování a přidání PDCP hlavičky, před předáním do [RLC](/mobilnisite/slovnik/rlc/) vrstvy. gNB provádí inverzní operaci. Funkce vyžaduje robustní mechanismy pro obnovu po chybě, aby zvládla ztrátu paketů bez způsobení desynchronizace kompresního kontextu.

UDC hraje klíčovou roli v optimalizaci využití rádiových zdrojů. Snížením velikosti přenosů ve směru uplink snižuje množství potřebných zdrojů fyzické vrstvy (bloků času/frekvence), což přímo vede ke zlepšení kapacity buňky a propustnosti uživatele. Je zvláště účinná pro aplikace s opakujícími se datovými vzory, jako jsou zprávy, hlášení IoT senzorů nebo některé webové protokoly. Funkci spravuje RAN a může být dynamicky řízena pro každé UE a každý bearer na základě síťové politiky a pozorovaných charakteristik provozu.

## K čemu slouží

UDC bylo vytvořeno, aby řešilo rostoucí asymetrii v mobilním datovém provozu a specifické výzvy přenosu ve směru uplink. Zatímco kapacita downlinku zaznamenala významná zlepšení díky pokročilým technikám, účinnost uplinku zůstávala úzkým hrdlem, omezeným vysílacím výkonem UE a dostupnou šířkou pásma. Přenos nezpracovaných, opakujících se dat (jako jsou hlavičky protokolů) zbytečně spotřebovává cenné rádiové zdroje a životnost baterie UE.

Tato technologie to řeší aplikací bezztrátové komprese u zdroje (UE), což přímo snižuje velikost datové části předtím, než spotřebuje zdroje rádiového rozhraní. To je zvláště důležité pro IoT zařízení tolerantní k latenci, která často odesílají malá, periodická hlášení, a pro scénáře s omezeným pokrytím uplink. Zlepšením spektrální účinnosti umožňuje UDC sítím obsloužit více uživatelů se stejným pásmem nebo poskytnout stejný uživatelský zážitek s nižší alokací zdrojů, což vede k úsporám nákladů a lepšímu výkonu. Jeho zavedení v LTE-Advanced (Rel-9) bylo součástí širšího úsilí o optimalizaci všech aspektů rádiového rozhraní pro efektivní zpracování dat.

## Klíčové vlastnosti

- Bezztrátová komprese na PDCP vrstvě pro uživatelská data ve směru uplink
- Dynamická konfigurace a aktivace prostřednictvím signalizace RRC
- Snižuje velikost IP paketů (hlaviček i datové části) před přenosem vzduchem
- Zlepšuje spektrální účinnost uplink a kapacitu buňky
- Snižuje spotřebu energie UE zkrácením doby vysílání
- Zahrnuje mechanismy pro synchronizaci kompresního kontextu a obnovu po chybě

## Související pojmy

- [PDCP – Packet Data Convergence Protocol](/mobilnisite/slovnik/pdcp/)
- [ROHC – Robust Header Compression](/mobilnisite/slovnik/rohc/)
- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TR 22.985** (Rel-19) — 3GPP User Data Convergence (UDC) concept
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.335** (Rel-19) — User Data Convergence (UDC) Procedures
- **TS 23.845** (Rel-10) — UDC Evolution Study
- **TS 23.862** (Rel-12) — Interworking Solutions for Mobile Operators & Data Apps
- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol
- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.214** (Rel-19) — Policy and Charging Control over Rx
- **TS 29.215** (Rel-19) — S9 Reference Point Stage 3 Specification
- **TR 29.935** (Rel-19) — HSS Reference Data Model for Ud Interface
- **TS 32.181** (Rel-19) — User Data Convergence Management Framework
- **TS 32.182** (Rel-19) — UDC Common Baseline Information Model (CBIM)
- **TR 32.901** (Rel-19) — UDC Application Data Models Study
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- … a dalších 10 specifikací

---

📖 **Anglický originál a plná specifikace:** [UDC na 3GPP Explorer](https://3gpp-explorer.com/glossary/udc/)
