---
slug: "iccid"
url: "/mobilnisite/slovnik/iccid/"
type: "slovnik"
title: "ICCID – Integrated Circuit Card Identification"
date: 2025-01-01
abbr: "ICCID"
fullName: "Integrated Circuit Card Identification"
category: "Identifier"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/iccid/"
summary: "Jedinečné sériové číslo trvale uložené v SIM (Subscriber Identity Module) nebo UICC (Universal Integrated Circuit Card) kartě. Identifikuje samotný fyzický hardware karty a je nezbytné pro správu inve"
---

ICCID je jedinečné sériové číslo trvale uložené v SIM nebo UICC kartě, které identifikuje fyzický hardware pro účely inventáře, personalizace a provizního připojení k síti.

## Popis

Integrated Circuit Card Identification (ICCID) je globálně jedinečné sériové číslo přidělené každé SIM nebo UICC kartě při výrobě. Definované doporučením [ITU-T](/mobilnisite/slovnik/itu-t/) E.118 a přijaté ve specifikacích 3GPP slouží jako primární identifikátor fyzického hardware, odlišný od identit účastníka jako je [IMSI](/mobilnisite/slovnik/imsi/) nebo [MSISDN](/mobilnisite/slovnik/msisdn/). ICCID má typicky délku 19 nebo 20 číslic, může však mít až 22 číslic a je strukturován tak, aby zahrnoval hlavní identifikátor odvětví (MII), identifikační číslo vydavatele (IIN), identifikaci individuálního účtu a kontrolní číslici vypočítanou pomocí Luhnova algoritmu. Toto číslo je fyzicky vyryto nebo vytištěno na kartě a je také elektronicky uloženo v nevolatilní paměti karty, konkrétně v elementárním souboru [EF](/mobilnisite/slovnik/ef/)_ICCID v rámci telekomunikačního souborového systému.

Z architektonického hlediska ICCID používají různé síťové a správní entity. Během počátečního procesu personalizace jej vydavatel karty (např. dodavatel SIM, mobilní operátor) používá ke sledování karty v průběhu jejího životního cyklu. V síti, přestože se nepoužívá pro běžné ověřování účastníka (to je role IMSI), může být ICCID přečteno mobilním zařízením a nahlášeno síti. Zařízení jej například může odeslat při určitých procedurách registrace nebo identifikace zařízení. Na platformě [OTA](/mobilnisite/slovnik/ota/) (Over-The-Air) je ICCID klíčovým adresovým tokenem, který OTA server používá k bezpečné identifikaci a cílení konkrétní karty UICC pro dálkovou správu aplikací, aktualizace souborů nebo provizní připojení profilů, jak je definováno v 3GPP TS 31.115.

Jeho role se rozšiřuje na správní systémy jako Equipment Identity Register ([EIR](/mobilnisite/slovnik/eir/)), kde může být použit spolu s [IMEI](/mobilnisite/slovnik/imei/) pro ověření párování zařízení a karty. V architekturách eSIM (embedded SIM) a dálkové SIM provize definovaných [GSMA](/mobilnisite/slovnik/gsma/) je ICCID základním identifikátorem pro vestavěný hardwarový prvek (eUICC) a pro profily na něj stažené. Toto číslo slouží jako neměnný referenční bod pro logistickou kontrolu, prevenci podvodů (např. detekci klonovaných karet, pokud je s jedním ICCID asociováno více aktivních IMSI) a jako záložní identifikátor v případě poškození dat účastníka. Je to kritická komponenta v celém dodavatelském řetězci a provozní správě modulů identity účastníka.

## K čemu slouží

ICCID byl vytvořen, aby poskytl jedinečný, trvalý a standardizovaný identifikátor pro každou fyzickou SIM kartu, čímž řeší potřebu efektivní správy inventáře, kontroly výroby a logistického sledování. Před touto standardizací bylo obtížné identifikovat jednotlivé karty ve výrobních várkách a operátorských zásobách. ICCID řeší problém jednoznačného rozlišení jedné karty od druhé v průběhu jejího globálního životního cyklu, od výroby a personalizace přes distribuci a aktivaci až po vyřazení.

Jeho vytvoření bylo motivováno expanzí GSM a potřebou robustního administrativního identifikátoru odděleného od účastníkově specifického IMSI. Toto oddělení je klíčové, protože SIM karta může být znovu personalizována pro různé účastníky (např. ve scénářích MVNO nebo při opětovném použití karty), ale fyzická karta zůstává stejná. ICCID poskytuje konstantní referenci pro hardware. Dále umožňuje klíčové provozní procesy: používá se při hromadných objednávkách SIM, v příkazech platformy OTA pro adresování konkrétní karty za účelem aktualizací a při párování s identifikátory zařízení pro rozšířené bezpečnostní služby. Řešil omezení dřívějších, méně formalizovaných identifikačních metod, které mohly vést k duplikaci nebo chybám ve sledování při rozsáhlých nasazeních, čímž podpořil škálovatelné, globální řízení stovek milionů SIM karet.

## Klíčové vlastnosti

- Globálně jedinečné sériové číslo pro každou fyzickou SIM/UICC kartu
- Trvale uloženo v nevolatilní paměti karty a vytištěno na těle karty
- Strukturované číslo v souladu s ITU-T E.118, obsahující identifikaci vydavatele a kontrolní číslici
- Používá se pro inventář karet, logistiku a sledování personalizace
- Slouží jako klíčový identifikátor pro správu OTA (Over-The-Air) a dálkové provizní připojení
- Poskytuje hardwarovou referenci odlišnou od identit účastníka, jako je IMSI

## Související pojmy

- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [OTA – Over The Air](/mobilnisite/slovnik/ota/)
- [EIR – Equipment Identity Register](/mobilnisite/slovnik/eir/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 27.007** (Rel-19) — AT Command Set for UE
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification
- **TS 33.110** (Rel-19) — UICC-Terminal Key Establishment

---

📖 **Anglický originál a plná specifikace:** [ICCID na 3GPP Explorer](https://3gpp-explorer.com/glossary/iccid/)
