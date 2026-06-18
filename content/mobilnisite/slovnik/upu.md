---
slug: "upu"
url: "/mobilnisite/slovnik/upu/"
type: "slovnik"
title: "UPU – UE Parameters Update"
date: 2025-01-01
abbr: "UPU"
fullName: "UE Parameters Update"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/upu/"
summary: "Bezpečnostní procedura v 5G, při které síť (AUSF/UDM) aktualizuje citlivé autentizační parametry uložené v modulu Universal Subscriber Identity Module (USIM) uživatelského zařízení (UE). Je spuštěna p"
---

UPU je bezpečnostní procedura v 5G, při které síť aktualizuje citlivé autentizační parametry v USIM uživatelského zařízení (UE). Je spuštěna při změně bezpečnostních politik nebo při ohrožení přihlašovacích údajů, aby zajistila aktuálnost klíčů.

## Popis

UE Parameters Update (UPU) je klíčová procedura údržby bezpečnosti definovaná v systému 5G (5GS). Jejím hlavním účelem je umožnit síťové autentizační funkci ([AUSF](/mobilnisite/slovnik/ausf/)) ve spolupráci s Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) proaktivně a bezpečně aktualizovat autentizační přihlašovací údaje uložené v aplikaci [USIM](/mobilnisite/slovnik/usim/) uživatelského zařízení (UE). Hlavními parametry, které lze aktualizovat, jsou dlouhodobý tajný klíč (K) a přidružené sekvenční číslo ([SQN](/mobilnisite/slovnik/sqn/)) používané v protokolech 5G Authentication and Key Agreement (5G-AKA) a Extensible Authentication Protocol ([EAP](/mobilnisite/slovnik/eap/))-AKA'. Procedura je architektonicky založena na AUSF, která generuje nový kryptografický materiál, a na UDM, která ukládá autentizační přihlašovací údaje účastníka.

Proceduru UPU iniciuje AUSF/UDM, obvykle na základě bezpečnostních politik operátora – například periodické rotace klíčů, detekce možného ohrožení přihlašovacích údajů nebo změny kryptografických algoritmů. Síť odešle zprávu UPU k uživatelskému zařízení (UE), která je bezpečně přenášena prostřednictvím obsluhující [AMF](/mobilnisite/slovnik/amf/) přes referenční bod N1. Tato zpráva obsahuje nové autentizační parametry (nový klíč K_new a SQN) zašifrované a chráněné integritou pomocí bezpečnostních klíčů odvozených ze *stávajících* přihlašovacích údajů sdílených mezi USIM a UDM. To zajišťuje, že pouze legitimní uživatelské zařízení (UE) může aktualizaci dešifrovat a zpracovat. Zásadně zpráva obsahuje [MAC](/mobilnisite/slovnik/mac/) (Message Authentication Code), který uživatelské zařízení (UE) ověří.

Po přijetí USIM uživatelského zařízení (UE) ověří MAC. Pokud je platný, nahradí starý klíč (K) a SQN novými hodnotami. USIM následně odešle potvrzení zpět do sítě. Celá tato transakce probíhá transparentně pro uživatele a hlavní procesor uživatelského zařízení (UE), protože je zpracována v bezpečném prostředí USIM. Specifikace 29.509 a 29.573 detailně popisují servisní rozhraní (Nausf_UEAuthentication, Nudm_UEAuthentication) používaná pro tento proces, zatímco 33.701 pokrývá bezpečnostní architekturu a procedury. Mechanismus UPU zajišťuje, že základní kořen důvěry pro přístup k síti může být obnoven bez nutnosti fyzické výměny [SIM](/mobilnisite/slovnik/sim/) karty, čímž je zachována dlouhodobá bezpečnostní integrita identifikátoru účastníka.

## K čemu slouží

UPU bylo zavedeno v 5G Release 15, aby vyřešilo významné bezpečnostní omezení předchozích generací mobilních sítí: statickou povahu dlouhodobého tajného klíče (K) uloženého na SIM/USIM. V sítích 2G, 3G a 4G byl tento klíč typicky zřízen jednou a po celou dobu trvání předplatného se neměnil, pokud nedošlo k fyzické výměně SIM karty. Tato statická povaha vytvářela rizika, včetně možnosti ohrožení klíče v čase prostřednictvím kryptografických útoků (opotřebení klíče) a neschopnosti efektivně reagovat, pokud bylo podezření na prolomení klíče.

Zavedení UPU tyto problémy řeší tím, že umožňuje vzdálenou, přenosovou (over-the-air) výměnu tohoto základního tajemství. To je motivováno potřebou silnější, proaktivní bezpečnosti v 5G, které podporuje kritickou infrastrukturu a služby. UPU umožňuje operátorům vynucovat politiky rotace klíčů, čímž zmírňuje riziko útoků využívajících dlouhodobé používání klíče. Poskytuje také efektivní nápravnou cestu, pokud je zjištěno, že konkrétní generátor klíčů je slabý, nebo pokud je konkrétní sada přihlašovacích údajů potenciálně ohrožena, a to bez logistického a uživatelského problému hromadné výměny SIM karet. Představuje posun směrem k dynamickému, řiditelnému bezpečnostnímu životnímu cyklu přihlašovacích údajů účastníka.

## Klíčové vlastnosti

- Bezpečně aktualizuje dlouhodobý tajný klíč (K) a sekvenční číslo (SQN) v USIM přenosově (over-the-air).
- Iniciována sítí (AUSF/UDM) na základě bezpečnostní politiky nebo reakce na hrozbu.
- Používá stávající přihlašovací údaje pro kryptografickou ochranu aktualizační zprávy, čímž zajišťuje, že ji může aplikovat pouze legitimní uživatelské zařízení (UE).
- Provedení je omezeno na bezpečné prostředí USIM, je transparentní vůči operačnímu systému uživatelského zařízení (UE).
- Poskytuje mechanismus potvrzení, který zajišťuje úspěšnou aplikaci aktualizace.
- Integruje se s architekturou 5G založenou na službách prostřednictvím servisních rozhraní AUSF a UDM.

## Definující specifikace

- **TS 29.509** (Rel-19) — AUSF Service Based Interface Protocol
- **TS 29.573** (Rel-19) — PLMN/SNPN Interconnection Interface Stage 3
- **TS 33.701** (Rel-19) — Study on mitigations against bidding down attacks

---

📖 **Anglický originál a plná specifikace:** [UPU na 3GPP Explorer](https://3gpp-explorer.com/glossary/upu/)
