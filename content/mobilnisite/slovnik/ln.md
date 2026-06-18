---
slug: "ln"
url: "/mobilnisite/slovnik/ln/"
type: "slovnik"
title: "LN – Logical Name"
date: 2025-01-01
abbr: "LN"
fullName: "Logical Name"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ln/"
summary: "Strukturovaný, lidsky čitelný identifikátor používaný v rámci systémů správy 3GPP k jednoznačnému pojmenování spravovaných objektů, síťových prvků nebo zdrojů. Řídí se hierarchickou konvencí pojmenová"
---

LN (Logický název) je strukturovaný, lidsky čitelný identifikátor používaný v rámci systémů správy 3GPP k jednoznačnému pojmenování spravovaných objektů, síťových prvků nebo zdrojů podle hierarchické konvence TMN.

## Popis

Logický název (Logical Name, LN) v 3GPP je základní konstrukcí v rámci rámců správy sítě, která poskytuje standardizovaný způsob identifikace a adresování spravovaných entit. Je definován jako Distinguished Name ([DN](/mobilnisite/slovnik/dn/)), který reprezentuje logickou identitu instance spravovaného objektu uvnitř Management Information Tree ([MIT](/mobilnisite/slovnik/mit/)). LN má hierarchickou strukturu, typicky složenou z Relative Distinguished Names ([RDN](/mobilnisite/slovnik/rdn/)), které specifikují atributy jako země, síť, operátor, typ zařízení a číslo instance. Tato konvence pojmenování je založena na standardech [ITU-T](/mobilnisite/slovnik/itu-t/) [TMN](/mobilnisite/slovnik/tmn/) (Telecommunication Management Network) a správy [OSI](/mobilnisite/slovnik/osi/) systémů (řada X.700). Architektonicky jsou LN používány systémy správy prvků ([EMS](/mobilnisite/slovnik/ems/)), systémy správy sítě ([NMS](/mobilnisite/slovnik/nms/)) a operačními podpůrnými systémy (OSS) k provádění funkcí FCAPS (Fault, Configuration, Accounting, Performance, Security). Například při konfiguraci základnové stanice nebo načítání výkonnostních čítačů se systém správy odkazuje na konkrétní entitu prostřednictvím jejího Logického názvu. LN je klíčový pro rozhraní správy založená na CORBA nebo na souborech definovaná v 3GPP, protože zajišťuje, že příkazy a data jsou správně směrovány k zamýšlenému síťovému zdroji. Funguje ve spojení s dalšími identifikátory, jako jsou ID fyzického zařízení, ale abstrahuje logickou funkci a síťovou roli. Hierarchická povaha umožňuje škálovatelnou správu, protože názvy mohou být přiřazovány na základě topologie sítě, což usnadňuje automatizované zřizování a správu inventáře.

## K čemu slouží

Koncept Logického názvu byl přijat k řešení problémů interoperability při správě složitých více-dodavatelských telekomunikačních sítí. Raná správa sítí často spoléhala na proprietární schémata pojmenování, což ztěžovalo a prodražovalo integraci mezi zařízeními různých dodavatelů a jejich systémy správy. LN, založený na principech TMN, poskytl standardizovaný, hierarchický model pojmenování, který umožňuje konzistentní identifikaci spravovaných objektů napříč různorodými síťovými prvky. Tím se vyřešilo omezení ad-hoc přístupů ke správě, což umožnilo automatizované OSS pracovní postupy, zjednodušenou izolaci poruch a jednotnou správu konfigurace. Historicky jeho zařazení do specifikací 3GPP (od Release 4 dále) podpořilo posun odvětví směrem ke standardizovaným Network Resource Models (NRM) a otevřeným rozhraním. Byl motivován potřebou škálovatelné provozní efektivity, jak se sítě vyvíjely z jedno-dodavatelského na heterogenní prostředí, a zajišťoval, že systémy správy mohou jednoznačně a spolehlivě adresovat každou konfigurovatelnou komponentu, od okruhově přepínaných uzlů po síťové funkce 5G.

## Klíčové vlastnosti

- Hierarchický, lidsky čitelný identifikátor dodržující konvence TMN
- Jednoznačně identifikuje instance spravovaných objektů v Management Information Tree
- Podporuje strukturované pojmenování s atributy (např. země, síť, typ zařízení)
- Umožňuje standardizované operace FCAPS napříč více-dodavatelskými sítěmi
- Používá se v rozhraních správy založených na CORBA a na souborech (např. Itf-N)
- Usnadňuje automatizované zřizování, správu inventáře a správu poruch

## Související pojmy

- [TMN – Telecommunications Management Network](/mobilnisite/slovnik/tmn/)
- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 33.851** (Rel-17) — Security for Industrial IoT in 5G

---

📖 **Anglický originál a plná specifikace:** [LN na 3GPP Explorer](https://3gpp-explorer.com/glossary/ln/)
