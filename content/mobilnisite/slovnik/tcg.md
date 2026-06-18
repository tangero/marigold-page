---
slug: "tcg"
url: "/mobilnisite/slovnik/tcg/"
type: "slovnik"
title: "TCG – Trusted Computing Group"
date: 2025-01-01
abbr: "TCG"
fullName: "Trusted Computing Group"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/tcg/"
summary: "Trusted Computing Group (TCG) je konsorcium, které vyvíjí a prosazuje otevřené, dodavatelsky neutrální, globální průmyslové standardy pro důvěryhodný hardware a software v oblasti trusted computing. V"
---

TCG je Trusted Computing Group, konsorcium, které vyvíjí otevřené standardy pro důvěryhodný hardware a software v oblasti trusted computing, na které 3GPP odkazuje pro bezpečnostní požadavky, jako je zabezpečené spuštění (secure boot) a vzdálené ověření integrity (remote attestation).

## Popis

Trusted Computing Group (TCG) není technologie specifická pro 3GPP, ale nezávislé průmyslové konsorcium, jehož standardy jsou přijímány a odkazovány ve specifikacích 3GPP za účelem zvýšení systémové bezpečnosti. Hlavním přínosem TCG je definice Trusted Platform Module (TPM), specializovaného mikrokontroléru navrženého pro zabezpečení hardwaru pomocí integrovaných kryptografických klíčů. V kontextu 3GPP poskytují standardy TCG základ pro vytvoření řetězce důvěry zakořeněného v hardwaru, což je klíčové pro procesy zabezpečeného spuštění (secure boot), ověření integrity platformy a vzdálené ověření integrity (remote attestation). Tím je zajištěno, že zařízení nebo síťová komponenta se spustí pouze s autorizovaným softwarem a zůstane v známém, důvěryhodném stavu, což chrání před útoky na firmware a neoprávněnými modifikacemi.

Architektura se točí kolem TPM, který obsahuje Endorsement Keys (EK), Storage Root Keys (SRK) a Platform Configuration Registers (PCR). EK je unikátní vestavěný kryptografický klíč identifikující TPM, zatímco SRK zabezpečuje klíče uložené v TPM. PCR uchovávají kryptograficky hashované hodnoty měření stavu platformy (např. BIOS, zavaděč, OS). Při zabezpečeném spuštění je každá komponenta změřena (hashována) a její hodnota je rozšířena do PCR před jejím spuštěním. Vzdálený ověřovatel může požadovat zprávu o ověření integrity (attestation report) – podepsané vyjádření hodnot PCR – k validaci integrity platformy. Tento proces je nedílnou součástí bezpečnostního rámce 3GPP pro zajištění důvěryhodných prostředí pro provádění (trusted execution environments) v uživatelských zařízeních (UE) a síťových funkcích.

V rámci 3GPP jsou principy TCG aplikovány ve specifikacích, jako je TS 33.812 (Studie bezpečnostních aspektů vzdálené provize a změny předplatného pro zařízení Machine to Machine) a TS 33.916 (Studie bezpečnostních aspektů 5G systému). Tyto dokumenty odkazují na standardy TCG pro definici požadavků na správu bezpečnostních prvků (secure element), ověření důvěryhodné platformy a hardwarovou bezpečnost pro IoT zařízení a 5G síťové vybavení. Tato integrace umožňuje systémům 3GPP využívat ověřené, standardizované mechanismy trusted computing, čímž zvyšuje celkovou odolnost sítě proti sofistikovaným útokům cílícím na integritu zařízení a autenticitu softwaru.

## K čemu slouží

Trusted Computing Group byla vytvořena, aby řešila rostoucí potřebu hardwarové bezpečnosti odolné proti softwarovým útokům. Tradiční bezpečnostní řešení založená pouze na softwaru jsou zranitelná, pokud je základní operační systém nebo firmware škodlivě změněn. Standardy TCG poskytují hardwarový kořen důvěry (hardware root of trust), což systémům umožňuje kryptograficky ověřovat svou vlastní integritu od samotného spuštění. To je klíčové pro moderní telekomunikace, kde musí být zařízením a síťovým prvkům důvěřováno při manipulaci s citlivými daty účastníků, provádění autentizace a plnění kritických síťových funkcí bez možnosti neoprávněného zásahu.

V 3GPP řeší odkazování na standardy TCG konkrétní problémy související s integritou zařízení a zabezpečenou provizí. Například ve scénářích Machine-to-Machine (M2M) a IoT (řešených v TS 33.812) vyžaduje vzdálená provize předplatného absolutní důvěru v bezpečnostní prvek (secure element) zařízení a jeho proces spuštění. Kompromitované zařízení by mohlo unést přihlašovací údaje nebo být naklonováno. Začleněním principů TCG zajišťuje 3GPP, že zařízení mohou prokázat svůj důvěryhodný stav před přijetím citlivých provozních dat. Podobně pro 5G systémy (TS 33.916) zvýšené využití virtualizace sítě a cloud-nativních funkcí vyžaduje robustní mechanismy pro ověření integrity hardwarových i softwarových platforem hostujících síťové funkce, což chrání před útoky v dodavatelském řetězci a zajišťuje dostupnost služeb.

Historicky se bezpečnost v mobilních sítích silně zaměřovala na kryptografické protokoly pro ochranu rozhraní (např. [AKA](/mobilnisite/slovnik/aka/)) a signalizaci v jádru sítě. Jak však útoky postupovaly a začaly cílit na firmware zařízení a platformní software, objevila se mezera v ověřování základní důvěryhodnosti prováděcího prostředí. Přijetí standardů TCG organizací 3GPP tuto mezeru zaplňuje tím, že poskytuje standardizovaný, interoperabilní rámec pro hardwarově podporovanou bezpečnost. To umožňuje dodavatelům a operátorům konzistentně implementovat funkce trusted computing v různorodých ekosystémech zařízení a infrastruktury, čímž se zvyšuje bezpečnostní jistota v stále složitější krajině hrozeb.

## Klíčové vlastnosti

- Definuje hardwarový kořen důvěry (hardware-based root of trust) prostřednictvím Trusted Platform Module (TPM)
- Specifikuje proces zabezpečeného spuštění (secure boot) s kryptografickým měřením každé softwarové komponenty
- Umožňuje vzdálené ověření integrity (remote attestation) pro ověření integrity platformy
- Poskytuje standardizovanou hierarchii kryptografických klíčů pro zabezpečené ukládání klíčů
- Podporuje zapečetěné úložiště (sealed storage) pro vázání dat na konkrétní stavy platformy
- Usnadňuje vytváření důvěryhodných prostředí pro provádění (trusted execution environments) citlivých operací

## Definující specifikace

- **TS 33.812** (Rel-9) — M2M Remote Subscription Management Security
- **TR 33.916** (Rel-19) — 3GPP Security Assurance Methodology (SECAM)

---

📖 **Anglický originál a plná specifikace:** [TCG na 3GPP Explorer](https://3gpp-explorer.com/glossary/tcg/)
