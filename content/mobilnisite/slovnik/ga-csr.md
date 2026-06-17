---
slug: "ga-csr"
url: "/mobilnisite/slovnik/ga-csr/"
type: "slovnik"
title: "GA-CSR – Generic Access - Circuit Switched Resources"
date: 2025-01-01
abbr: "GA-CSR"
fullName: "Generic Access - Circuit Switched Resources"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ga-csr/"
summary: "Komponenta standardu Generic Access Network (GAN) / UMA, která umožňuje mobilnímu zařízení přistupovat k tradičním GSM službám s přepojováním okruhů (jako je hlas a SMS) přes nelicencovanou bezdrátovo"
---

GA-CSR je komponenta standardu Generic Access Network (GA-N), který umožňuje přístup ke klasickým GSM službám s přepojováním okruhů, jako je hlas a SMS, přes nelicencovanou bezdrátovou IP síť jako je Wi-Fi.

## Popis

Generic Access - Circuit Switched Resources (GA-CSR) je klíčová funkční komponenta v architektuře Generic Access Network ([GAN](/mobilnisite/slovnik/gan/)) podle 3GPP, dříve známá jako Unlicensed Mobile Access (UMA). GA-CSR specificky zajišťuje navazování, udržování a ukončování spojení s přepojováním okruhů přes IP přístupovou síť. Když se uživatelské zařízení (UE) připojí přes přístupový bod Wi-Fi, funkce GA-CSR mu umožní registrovat se v jádrové síti a využívat klasické služby s přepojováním okruhů, jako by bylo připojeno přímo k GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)).

Z architektonického hlediska GA-CSR funguje uvnitř Generic Access Network Controlleru ([GANC](/mobilnisite/slovnik/ganc/)) nebo vyvinutého Wireless [LAN](/mobilnisite/slovnik/lan/) Controlleru (eWLC) v novějších specifikacích. UE obsahuje vrstvu Generic Access ([GA](/mobilnisite/slovnik/ga/)), která zapouzdřuje GSM signalizaci a datový provoz (např. hlasové rámce) do IP paketů (s použitím protokolů jako IKEv2 a [IPSec](/mobilnisite/slovnik/ipsec/) pro zabezpečení). Tyto pakety jsou tunelovány přes širokopásmové IP připojení k GANC. GANC prostřednictvím své GA-CSR funkce pak tuto komunikaci de-encapsuluje a předává ji jádrové síti směrem k Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) pomocí standardních protokolů A-interface nebo Iu-cs interface. MSC si není vědomo IP přístupové větve; vnímá UE jako obsluhované standardním BSS.

Funkce GA-CSR zajišťuje klíčové procedury, jako je GA-CSR registrace, kdy se UE ohlásí přes IP; GA-CSR deregistrace; a handover pro přepojování okruhů, umožňující hladké přechody mezi Wi-Fi a mobilním pokrytím během hovorů. Logicky spravuje rádiové zdroje, překládá parametry IP přenosu do konceptů zdrojů s přepojováním okruhů (jako časové sloty a kanály pro přenos hovorů), které očekává jádrová síť. Tato abstrakce je zásadní pro kontinuitu služeb a transparentnost sítě.

## K čemu slouží

GA-CSR byl vytvořen k řešení problému špatného pokrytí mobilní sítě v interiérech, zejména pro hlasové služby, prostřednictvím využití všudypřítomnosti Wi-Fi a širokopásmového internetu. Před GAN/GA-CSR museli operátoři pro zlepšení vnitřního pokrytí nasazovat nákladné mikrobuňky nebo femtobuňky. GA-CSR poskytl standardizovanou, nákladově efektivní alternativu, která využívala stávající Wi-Fi síť účastníka v domácnosti nebo podniku jako de facto přístupový bod mobilní sítě.

Řešil omezení dvoupásmových telefonů, které mohly používat Wi-Fi pro data (pomocí I-WLAN), ale ne pro nativní hlasovou telefonii. GA-CSR umožnil skutečnou konvergenci pevných a mobilních sítí (FMC) pro služby s přepojováním okruhů, což účastníkům dovolovalo uskutečňovat a přijímat standardní GSM hlasové hovory a SMS přes Wi-Fi. To byl významný faktor pro přijetí mezi zákazníky, protože poskytoval jediné telefonní číslo a jednotný zážitek ze služeb bez ohledu na podkladovou přístupovou technologii.

Technologie byla motivována komerčním úspěchem prvních nasazení UMA a byla standardizována 3GPP od Release 6 výše (s klíčovými specifikacemi v Release 8). Umožnila mobilním síťovým operátorům (MNO) bránit své příjmy z klíčových hlasových služeb proti konkurenci Voice over IP (VoIP) tím, že nabídli kvalitní, bezproblémový zážitek z volání přes Wi-Fi přímo integrovaný do jejich stávající jádrové sítě s přepojováním okruhů a systémů podpory podnikání.

## Klíčové vlastnosti

- Umožňuje GSM/UMTS hlasové služby a službu SMS s přepojováním okruhů přes nelicencovaný IP přístup (např. Wi-Fi)
- Poskytuje plynulý handover aktivních hovorů mezi Wi-Fi a mobilními sítěmi
- Využívá IPSec tunely pro zabezpečený přenos signalizace a datové roviny pro přepojování okruhů
- Vystupuje vůči jádrovému MSC jako standardní BSS přes A-interface
- Podporuje specifické procedury GA-CSR: Registraci, Deregistraci a Handover
- Transparentní pro jádrovou síť; služby jsou identické jako při přístupu přes mobilní síť

## Související pojmy

- [GANC – Generic Access Network Controller](/mobilnisite/slovnik/ganc/)

## Definující specifikace

- **TS 43.318** (Rel-19) — Generic Access Network (GAN) Stage 2
- **TR 43.902** (Rel-19) — GAN Enhancements Feasibility Study
- **TS 44.318** (Rel-19) — Generic Access Network (GAN) Interface Procedures

---

📖 **Anglický originál a plná specifikace:** [GA-CSR na 3GPP Explorer](https://3gpp-explorer.com/glossary/ga-csr/)
