---
slug: "sgw-pgw"
url: "/mobilnisite/slovnik/sgw-pgw/"
type: "slovnik"
title: "SGW/PGW – Serving Gateway / Packet Data Network Gateway"
date: 2025-01-01
abbr: "SGW/PGW"
fullName: "Serving Gateway / Packet Data Network Gateway"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sgw-pgw/"
summary: "SGW a PGW jsou klíčové uzly v Evolved Packet Core (EPC) pro sítě 4G LTE. SGW směruje a přeposílá pakety uživatelských dat a slouží jako kotva pro mobilitu při předávání spojení. PGW zajišťuje připojen"
---

SGW/PGW je kombinovaná brána Serving Gateway a Packet Data Network Gateway v jádru sítě 4G LTE, kde SGW směruje uživatelská data a zajišťuje kotvu pro mobilitu, zatímco PGW se připojuje k externím sítím a přiděluje IP adresy.

## Popis

Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)) a Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) jsou základními komponentami architektury Evolved Packet Core (EPC) pro 4G LTE, definovanými od 3GPP Release 8 výše. V síťových implementacích jsou často umístěny společně a označovány jako S/[P-GW](/mobilnisite/slovnik/p-gw/). SGW je kotvou uživatelské roviny pro mobilitu v rámci LTE (např. předání spojení mezi eNodeB) a mezi různými 3GPP technologiemi (např. předání spojení do sítí 2G/3G). Spravuje a uchovává kontexty uživatelských zařízení (UE), včetně parametrů služby IP přenosu a informací o interním směrování sítě. Všechny uživatelské IP pakety jsou směrovány přes SGW. Rozhraní SGW s eNodeB je [S1-U](/mobilnisite/slovnik/s1-u/) a s ostatními SGW je S5/S8 pro předání spojení. SGW také generuje účtovací data pro každé UE a připojení [PDN](/mobilnisite/slovnik/pdn/) pro potřeby účtovací funkce.

Packet Data Network Gateway (PGW) je výstupním a vstupním bodem pro provoz UE směrem k externím paketovým datovým sítím (PDN), jako je internet nebo IMS síť. Slouží jako kotva pro mobilitu mezi 3GPP a ne-3GPP technologiemi (např. Wi-Fi). Mezi klíčové funkce patří přidělování IP adres pro UE (pomocí [DHCP](/mobilnisite/slovnik/dhcp/) nebo z externího [AAA](/mobilnisite/slovnik/aaa/) serveru), vynucování politik a tokové účtování podle pokynů funkce Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)), filtrování paketů a podpora zákonného odposlechu. PGW provádí hlubokou inspekci paketů, aby mohla uplatňovat pravidla politik a účtování. Připojuje se k SGW přes rozhraní S5 (v neramingovém scénáři) nebo S8 (v roamingovém scénáři) a k externím sítím přes rozhraní SGi.

SGW a PGW společně zajišťují celou cestu uživatelských dat. SGW se zaměřuje na správu mobility a směrování v rámci 3GPP sítě, zatímco PGW spravuje externí připojení, politiky a účtování. V řídicí rovině komunikují s Mobility Management Entity (MME) přes rozhraní S11 pro správu přenosů a s PCRF přes rozhraní Gx pro řízení politik a účtování. Jejich kombinovaná role je klíčová pro zajištění plynulé mobility, kvality služeb a bezpečného, zpoplatnitelného přístupu k internetu pro mobilní účastníky.

## K čemu slouží

SGW a PGW byly zavedeny spolu s Evolved Packet System (EPS) v 3GPP Release 8 za účelem vytvoření zjednodušeného, plně IP jádra sítě pro LTE. Nahradily komplexní sadu uzlů jádra sítí 2G a 3G (jako SGSN a GGSN) plošší a efektivnější architekturou optimalizovanou pro vysokorychlostní paketová data. Primárním cílem bylo snížení latence, zvýšení datové propustnosti a podpora trvalého připojení, což byla omezení předchozích 3GPP architektur původně navržených pro okruhově spínanou hlasovou službu.

Oddělení funkcí SGW a PGW umožňuje flexibilní nasazení sítě. SGW může být distribuována blíže k rádiové síti, aby se optimalizovala cesta uživatelských dat a snížila latence pro lokální provoz. PGW může být centralizována pro efektivní správu politik, účtování a připojení k více externím sítím. Tato architektura vyřešila problém neefektivního směrování dat v dřívějších sítích a poskytla jasnou kotvu pro mobilitu a vynucování politik, což bylo nezbytné pro umožnění nových služeb, jako je VoIP přes LTE (VoLTE) a kvalitní mobilní širokopásmový přístup.

## Klíčové vlastnosti

- Kotva uživatelské roviny pro mobilitu v rámci LTE a mezi 3GPP technologiemi (SGW)
- Brána k externím paketovým datovým sítím, jako je internet (PGW)
- Vynucování politik a řízení tokového účtování (PGW)
- Přidělování IP adres pro uživatelské zařízení (UE) (PGW)
- Podpora zákonného odposlechu
- Správa přenosů na základě požadavků QoS

## Související pojmy

- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)

## Definující specifikace

- **TS 22.278** (Rel-19) — Evolved Packet System Service Requirements
- **TS 22.803** (Rel-12) — Proximity Services (ProSe) Study

---

📖 **Anglický originál a plná specifikace:** [SGW/PGW na 3GPP Explorer](https://3gpp-explorer.com/glossary/sgw-pgw/)
