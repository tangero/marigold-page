---
slug: "ch1"
url: "/mobilnisite/slovnik/ch1/"
type: "slovnik"
title: "CH1 – CTS Random Challenge Value of the CTS-FP"
date: 2025-01-01
abbr: "CH1"
fullName: "CTS Random Challenge Value of the CTS-FP"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ch1/"
summary: "CH1 je náhodná výzva používaná v autentizačním protokolu systému bezšňůrové telefonie – pevná část (CTS-FP). Slouží jako kryptografický nonce k zabránění opakovaným útokům během autentizačního procesu"
---

CH1 je náhodná výzva (challenge) používaná jako kryptografický nonce v autentizačním protokolu systému bezšňůrové telefonie – pevná část (Cordless Telephony System - Fixed Part) k zabránění opakovaným útokům (replay attacks) mezi mobilní stanicí a pevnou sítí.

## Popis

CH1 je klíčová součást protokolu pro autentizaci a dohodu klíčů ([AKA](/mobilnisite/slovnik/aka/)) specifikovaného pro systém bezšňůrové telefonie – pevná část ([CTS-FP](/mobilnisite/slovnik/cts-fp/)) v dokumentu 3GPP TS 43.020. Funguje jako náhodná výzva generovaná autentizačním centrem sítě (AuC) nebo odpovídající entitou pevné sítě. Tato hodnota je přenášena k mobilní stanici ([MS](/mobilnisite/slovnik/ms/)) během autentizační procedury, aby zahájila kryptografickou výměnu, která ověří identitu obou stran a naváže bezpečné relací klíče.

Technický postup zahrnuje generování CH1 sítí jako náhodného čísla (typicky 128 bitů) a jeho odeslání k mobilní stanici spolu s dalšími autentizačními parametry. Mobilní stanice použije tuto hodnotu CH1 spolu se sdíleným tajným klíčem (Ki) a dalšími síťově specifickými daty jako vstup kryptografických algoritmů (původně variant COMP128) k výpočtu odpovědi (SRES) a šifrovacího klíče (Kc). Mobilní stanice vrátí hodnotu SRES síti, která provede stejný výpočet nezávisle. Pokud se vypočtené hodnoty SRES shodují, autentizace uspěje a odvozený klíč Kc je použit pro šifrování následné komunikace.

Z architektonického hlediska je CH1 součástí mechanismu výzva-odpověď, který brání opakovaným útokům. Tím, že zajišťuje, aby každá hodnota CH1 byla náhodná a použita pouze jednou v rámci své platnosti, systém garantuje, že odposlechnutá autentizační sekvence nemůže být útočníkem znovu použita. Generování CH1 vyžaduje kryptograficky bezpečný generátor náhodných čísel v rámci bezpečnostní infrastruktury sítě. Integrita hodnoty během přenosu je chráněna, ačkoli v raných implementacích [CTS](/mobilnisite/slovnik/cts/) mohla tato ochrana spoléhat spíše na inherentní obtížnost předpovědi náhodné sekvence než na šifrování samotné výzvy.

Role CH1 přesahuje pouhou autentizaci; je to základ (seed) pro celý proces odvozování klíčů. Náhodnost a nepředvídatelnost CH1 přímo ovlivňuje sílu odvozeného relací klíče Kc. Slabá nebo předvídatelná hodnota CH1 by mohla ohrozit bezpečnost celé relace. V rámci protokolového zásobníku CTS-FP je CH1 přenášena v konkrétních signalizačních zprávách pro autentizaci mezi řadičem pevné sítě a mobilním přístrojem, podle protokolů definovaných pro propojení [DECT](/mobilnisite/slovnik/dect/)/GSM specifikované v TS 43.020.

## K čemu slouží

CH1 bylo vytvořeno za účelem poskytnutí bezpečného autentizačního mechanismu pro systémy bezšňůrové telefonie ([CTS](/mobilnisite/slovnik/cts/)), které spolupracují se sítěmi GSM, jak je standardizováno ve 3GPP Release 8. Před standardizovaným propojením často proprietární bezšňůrové systémy používaly slabší nebo žádnou autentizaci, což je činilo zranitelnými vůči klonování a neoprávněnému přístupu. Specifikace [CTS-FP](/mobilnisite/slovnik/cts-fp/) si kladla za cíl přinést bezpečnost na úrovni GSM do prostředí bezšňůrové telefonie, zejména pro rezidenční a firemní základnové stanice připojené k veřejné síti.

Základní problém, který CH1 řeší, je potřeba vzájemné autentizace a bezpečného navázání klíčů v jednoduchém a cenově efektivním bezšňůrovém systému. Bez náhodné výzvy, jako je CH1, by autentizační protokoly mohly být náchylné k opakovaným útokům, kdy útočník zaznamená legitimní autentizační výměnu a zopakuje ji pro získání přístupu k síti. Zavedením jedinečné, sítí generované náhodné hodnoty pro každý pokus o autentizaci systém zajišťuje aktuálnost a těmto útokům brání.

Historický kontext zahrnuje konvergenci technologie [DECT](/mobilnisite/slovnik/dect/) (Digital Enhanced Cordless Telecommunications) se zásadami zabezpečení jádrové sítě GSM. CTS-FP umožnilo DECT přístrojům autentizovat se pomocí GSM SIM karet a algoritmů. Návrh CH1 následuje vzor GSM AKA, ale přizpůsobuje ho architektuře CTS, čímž řeší omezení statických autentizačních tokenů zavedením dynamických, relaci specifických výzev. To umožnilo bezpečná bezšňůrová rozšíření sítí GSM při zachování kompatibility s existujícími moduly identifikace účastníka (SIM) a autentizační infrastrukturou.

## Klíčové vlastnosti

- Generování náhodného čísla pro zajištění kryptografické aktuálnosti
- Zabránění opakovaným útokům (replay attacks) na autentizaci
- Vstupní hodnota (seed) pro odvození šifrovacího klíče (Kc)
- Integrace s autentizačními algoritmy GSM (COMP128)
- Součást protokolu výzva-odpověď v CTS-FP
- Umožňuje vzájemnou autentizaci mezi mobilní a pevnou částí

## Související pojmy

- [CTS-FP – Cordless Telephony System - Fixed Part](/mobilnisite/slovnik/cts-fp/)

## Definující specifikace

- **TS 43.020** (Rel-19) — Security Procedures for GSM

---

📖 **Anglický originál a plná specifikace:** [CH1 na 3GPP Explorer](https://3gpp-explorer.com/glossary/ch1/)
