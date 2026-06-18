---
slug: "h-rnti"
url: "/mobilnisite/slovnik/h-rnti/"
type: "slovnik"
title: "H-RNTI – HS-DSCH Radio Network Temporary Identifier"
date: 2025-01-01
abbr: "H-RNTI"
fullName: "HS-DSCH Radio Network Temporary Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/h-rnti/"
summary: "HS-DSCH Radio Network Temporary Identifier (H-RNTI) je uživatelským zařízením (UE) specifický identifikátor používaný v sítích UMTS/HSPA pro adresování uživatele na vysokorychlostním společném kanálu"
---

H-RNTI je uživatelským zařízením (UE) specifický identifikátor přidělený Node B v sítích UMTS/HSPA pro adresování uživatele na vysokorychlostním společném kanálu pro přenos dat v downlinku (HS-DSCH) za účelem plánování a přenosu dat.

## Popis

[HS-DSCH](/mobilnisite/slovnik/hs-dsch/) Radio Network Temporary Identifier (H-RNTI) je klíčový identifikátor v rádiových přístupových sítích UMTS (Universal Mobile Telecommunications System) a [HSPA](/mobilnisite/slovnik/hspa/) (High-Speed Packet Access). Je to 16bitová hodnota, která je jednoznačně přidělena uživatelskému zařízení (UE) Node B (základnovou stanicí) po dobu trvání spojení na vysokorychlostním společném kanálu pro přenos dat v downlinku (HS-DSCH). H-RNTI slouží k adresování UE na tomto sdíleném downlink přenosovém kanálu, což Node B umožňuje směrovat přenosy dat HS-DSCH konkrétně k danému UE mezi mnoha uživateli sdílejícími stejné kanálové zdroje.

Architektonicky H-RNTI funguje v rámci vrstvy [MAC](/mobilnisite/slovnik/mac/) (Medium Access Control), konkrétně entity MAC-hs v Node B a entity MAC-hs v UE. Když je UE nakonfigurováno pro službu [HSDPA](/mobilnisite/slovnik/hsdpa/) (High-Speed Downlink Packet Access), [RNC](/mobilnisite/slovnik/rnc/) (Radio Network Controller) instruuje Node B, aby zřídilo rádiové spojení HS-DSCH. Node B následně přidělí UE H-RNTI a toto přidělení komunikuje prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/) (Radio Resource Control) z RNC. H-RNTI je obsaženo v příkazech na [HS-SCCH](/mobilnisite/slovnik/hs-scch/) (High-Speed Shared Control Channel) a v hlavičkách protokolových datových jednotek MAC-hs k identifikaci zamýšleného příjemce dat na [HS-PDSCH](/mobilnisite/slovnik/hs-pdsch/) (High-Speed Physical Downlink Shared Channel).

H-RNTI funguje tak, že je vestavěno do řídicích a datových přenosů. V downlinku Node B používá HS-SCCH k odesílání řídicích informací (jako je transportní formát a HARQ data) jeden slot před odpovídajícím přenosem na HS-PDSCH. Tyto řídicí informace jsou zakódovány (scramblovány) pomocí H-RNTI. UE nepřetržitě monitoruje HS-SCCH, aby detekovalo řídicí zprávy zakódované jeho přiřazeným H-RNTI. Po detekci UE ví, že má dekódovat následný přenos na HS-PDSCH. V hlavičce MAC-hs datového paketu na HS-PDSCH je také obsaženo H-RNTI, aby si UE mohlo ověřit cílového příjemce paketu. Tento dvoukrokový proces – indikace na řídicím kanálu následovaná přenosem na datovém kanálu – umožňuje efektivní provoz sdíleného kanálu.

Mezi klíčové součásti patří HS-SCCH pro řídicí signalizaci, HS-PDSCH pro přenos dat, MAC-hs pro plánování paketů a multiplexování a RRC pro signalizaci přidělení H-RNTI. Role H-RNTI je zásadní pro mechanismus plánování v HSDPA. Umožňuje Node B provádět rychlé plánování závislé na stavu kanálu přímo (bez účasti RNC pro každý přenos), což výrazně snižuje latenci a zvyšuje propustnost v downlinku. Díky jednoznačné identifikaci UE na sdíleném kanálu umožňuje multiplexování více uživatelů v časové i kódové doméně a optimalizuje tak využití rádiových zdrojů v sítích UMTS/HSPA.

## K čemu slouží

H-RNTI bylo zavedeno ve 3GPP Release 5 jako součást sady funkcí HSDPA pro UMTS. Bylo vytvořeno, aby vyřešilo omezení původního downlinku UMTS Release 99, který používal pro paketová data vyhrazené kanály (DCH), což vedlo k neefektivnímu využívání zdrojů a vyšší latenci. Release 99 vyžadovalo, aby RNC spravovalo plánování, což bylo pomalé a nemohlo se rychle přizpůsobovat náhlým změnám stavu kanálu.

Primárním motivem pro zavedení H-RNTI bylo umožnit rychlé plánování řízené Node B na sdíleném downlink kanálu, což je klíčová inovace HSDPA. Přidělením dočasného identifikátoru (H-RNTI) každému aktivnímu uživateli HSDPA mohlo Node B přímo adresovat UE na HS-DSCH bez nutnosti signalizace od RNC pro každý přenos. Tím se snížila režie řídicí komunikace a latence, což umožnilo provádět rozhodnutí o plánování každých 2 ms (Transmission Time Interval – TTI) na základě okamžité zpětné vazby o kvalitě kanálu od UE.

Dále H-RNTI vyřešilo problém efektivního multiplexování více uživatelů na sdíleném zdroji. V kombinaci s HS-SCCH poskytlo odlehčený adresovací mechanismus, který umožnil časový a kódový multiplex na HS-PDSCH. To bylo nezbytné pro maximalizaci propustnosti buňky a podporu většího počtu vysokorychlostních datových uživatelů. Koncept H-RNTI byl klíčovým prvkem umožňujícím výkonnostní zisky HSPA, což dovolilo sítím UMTS konkurovat nově vznikajícím širokopásmovým technologiím díky výraznému zvýšení datových rychlostí v downlinku a spektrální účinnosti.

## Klíčové vlastnosti

- 16bitový uživatelskému zařízení (UE) specifický identifikátor pro adresování na HS-DSCH v UMTS/HSPA
- Přidělen Node B a signalizován UE prostřednictvím RRC z RNC
- Použit ke kódování (scramblování) řídicích informací na HS-SCCH pro identifikaci UE
- Obsažen v hlavičkách MAC-hs pro ověření cíle datového paketu
- Umožňuje rychlé plánování řízené Node B s granularitou TTI 2 ms
- Podporuje multiplexování více uživatelů na sdíleném HS-PDSCH

## Související pojmy

- [HS-DSCH – High Speed Downlink Shared Channel](/mobilnisite/slovnik/hs-dsch/)
- [HS-SCCH – High Speed Physical Downlink Shared Control Channel](/mobilnisite/slovnik/hs-scch/)
- [HS-PDSCH – High Speed Physical Downlink Shared Channel](/mobilnisite/slovnik/hs-pdsch/)
- [UE – User Equipment](/mobilnisite/slovnik/ue/)

## Definující specifikace

- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [H-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/h-rnti/)
