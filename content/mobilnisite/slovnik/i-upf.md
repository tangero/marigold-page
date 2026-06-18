---
slug: "i-upf"
url: "/mobilnisite/slovnik/i-upf/"
type: "slovnik"
title: "I-UPF – Intermediate User Plane Function"
date: 2026-01-01
abbr: "I-UPF"
fullName: "Intermediate User Plane Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/i-upf/"
summary: "I-UPF je funkce uživatelské roviny nasazená lokálně v síti 5G, která poskytuje bod výstupu pro přenos dat uživatele, čímž snižuje latenci a zatížení páteřní sítě. Je řízena funkcí Intermediate SMF (I-"
---

I-UPF je lokálně nasazená funkce uživatelské roviny v síti 5G, která poskytuje bod výstupu pro přenos dat uživatele za účelem snížení latence a zatížení páteřní sítě.

## Popis

Intermediate User Plane Function (I-UPF) je klíčový prvek uživatelské roviny v 5G páteřní síti (5GC), standardizovaný od 3GPP Release 16. Představuje specifickou instanci nasazení [UPF](/mobilnisite/slovnik/upf/), která není kotvícím bodem relace. Místo toho je I-UPF vložena do cesty uživatelské roviny mezi rádiovou přístupovou sítí (RAN) – nebo jinou přístupovou sítí – a Anchor UPF (A-UPF). Typicky je umístěna společně s přístupovým bodem nebo v jeho blízkosti, aby umožnila lokální zpracování a směrování dat.

Architektonicky je I-UPF řízena funkcí Intermediate Session Management Function ([I-SMF](/mobilnisite/slovnik/i-smf/)) přes rozhraní N4. I-SMF s I-UPF naváže relaci N4 a zřídí v ní pravidla pro detekci paketů ([PDR](/mobilnisite/slovnik/pdr/)), pravidla pro přeposílání ([FAR](/mobilnisite/slovnik/far/)), pravidla pro reportování využití ([URR](/mobilnisite/slovnik/urr/)) a pravidla pro vynucení QoS ([QER](/mobilnisite/slovnik/qer/)) specifická pro potřeby lokálního směrování provozu. I-UPF provádí standardní funkce UPF, jako je inspekce paketů, ukotvování a přeposílání, ale v lokálním kontextu. Jejím klíčovým operačním úkolem je sloužit jako první bod ukončení uživatelské roviny od přístupové sítě (přes rozhraní N3 nebo N9') a přeposílat provoz směrem k A-UPF (přes rozhraní N9) nebo lokálně vyvést provoz do datové sítě ([DN](/mobilnisite/slovnik/dn/)) přes rozhraní N6, pokud je lokálně nasazena.

Funkcionalita I-UPF je klíčová pro několik paradigmat 5G. V mobilních scénářích, zejména když se uživatelské zařízení (UE) přesune z 3GPP přístupu na non-3GPP přístup (jako [WLAN](/mobilnisite/slovnik/wlan/)), může být I-UPF vložena, aby poskytla lokální cestu uživatelské roviny bez změny A-UPF, a zachovala tak kontinuitu relace. Pro edge computing poskytuje I-UPF nízkolatenční spojení k lokálním aplikačním serverům. Hraje také zásadní roli ve funkcionalitách UL CL (Uplink Classifier) a BP (Branching Point) definovaných pro ATSSS, což umožňuje směrovat nebo rozdělovat provoz přes více přístupů nebo cest. Lokálním zpracováním a směrováním provozu I-UPF odlehčuje páteřní přenosovou síť, snižuje celkovou latenci a umožňuje efektivní poskytování služeb přizpůsobené geografické poloze UE.

## K čemu slouží

I-UPF byla zavedena v Release 16, aby řešila potřebu flexibilnější a distribuovanější architektury uživatelské roviny v 5G, což bylo omezení v dřívějších návrzích páteřní sítě. V počáteční architektuře 5G Release 15 byla PDU relace typicky ukotvena v jediné UPF. Ačkoli to zjednodušilo správu, nutilo to veškerý provoz uživatelské roviny, i ten určený pro lokální server, procházet páteřní sítí ke kotvícímu bodu a zpět, což vytvářelo 'trombone efekt'. To bylo neefektivní pro nízkolatenční aplikace, edge computing a lokalizované služby.

Koncept I-UPF to řeší tím, že umožňuje řetězec UPF. Umožňuje síťovým operátorům nasadit UPF na okraji sítě, blízko uživatelů a aplikačních serverů. I-UPF zvládá lokální výstup provozu, zatímco A-UPF zůstává stabilní kotvou pro relaci, zajišťující zachování IP adresy a kontinuitu během mobility. To je obzvláště důležité pro případy užití, jako je automatizace továren, rozšířená realita a efektivní konvergence pevných a mobilních sítí, kde záleží na milisekundách latence. I-UPF pod kontrolou I-SMF poskytuje topologickou agilitu potřebnou k dynamické optimalizaci datové cesty na základě polohy UE, požadavků služby a stavu sítě, čímž řeší rigidní směrování uživatelské roviny předchozích generací.

## Klíčové vlastnosti

- Poskytuje lokální zpracování uživatelské roviny a výstup provozu v blízkosti přístupové sítě
- Řízena funkcí I-SMF přes rozhraní N4 pro relací specifická pravidla
- Podporuje rozhraní N3 (přístup) a N9 (mezi UPF) a volitelně lokální rozhraní N6
- Umožňuje funkce UL CL (Uplink Classifier) a BP (Branching Point) pro ATSSS
- Snižuje latenci a zatížení páteřní přenosové sítě lokalizací tras provozu
- Nezbytná pro umožnění Multi-Access Edge Computing (MEC) a nízkolatenčních služeb

## Související pojmy

- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [I-SMF – Intermediate Session Management Function](/mobilnisite/slovnik/i-smf/)
- [ATSSS – Access Traffic Steering, Switching, and Splitting](/mobilnisite/slovnik/atsss/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TR 23.726** (Rel-16) — SMF/UPF Topology Enhancements in 5G
- **TR 28.833** (Rel-18) — Technical Report on 5G LAN-type Service Management
- **TS 29.892** (Rel-16) — Study on User Plane Protocol in 5GC

---

📖 **Anglický originál a plná specifikace:** [I-UPF na 3GPP Explorer](https://3gpp-explorer.com/glossary/i-upf/)
