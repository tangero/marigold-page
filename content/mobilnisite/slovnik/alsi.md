---
slug: "alsi"
url: "/mobilnisite/slovnik/alsi/"
type: "slovnik"
title: "ALSI – Application Level Subscriber Identity"
date: 2025-01-01
abbr: "ALSI"
fullName: "Application Level Subscriber Identity"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/alsi/"
summary: "ALSI je identifikátor účastníka používaný na aplikační vrstvě k jednoznačné identifikaci uživatelů napříč různými službami a aplikacemi. Umožňuje poskytovatelům služeb spravovat identity uživatelů nez"
---

ALSI (Application Level Subscriber Identity) je identifikátor účastníka na aplikační vrstvě, který slouží k jednoznačné identifikaci uživatelů napříč různými službami a umožňuje správu identity nezávislou na síťových identifikátorech.

## Popis

Application Level Subscriber Identity (ALSI) je klíčový identifikátor v systémech 3GPP, který funguje na aplikační vrstvě a je oddělený od síťových identifikátorů, jako je [IMSI](/mobilnisite/slovnik/imsi/) nebo [MSISDN](/mobilnisite/slovnik/msisdn/). Na rozdíl od síťových identifikátorů vázaných na [SIM](/mobilnisite/slovnik/sim/) karty nebo síťová předplatné poskytuje ALSI identitu specifickou pro službu, kterou lze využívat napříč více aplikacemi a službami. Toto oddělení umožňuje poskytovatelům aplikací udržovat vlastní systémy správy identity a zároveň při potřebě pro účely autentizace nebo fakturace korelovat uživatele s jejich síťovými identitami.

Architektura podporující ALSI zahrnuje koordinaci mezi aplikační vrstvou a podkladovou síťovou infrastrukturou. Když uživatel přistupuje ke službě, může aplikační server prostřednictvím standardizovaných rozhraní s jádrem sítě požádat o autentizaci pomocí ALSI. Síť následně namapuje ALSI na odpovídající síťový identifikátor (jako je IMSI), aby ověřila stav předplatného a oprávnění uživatele. Toto mapování typicky spravují autentizační servery a systémy správy identity, které udržují vztahy mezi identitami na aplikační a síťové úrovni.

ALSI funguje na principu vícevrstvého přístupu ke správě identity, kde aplikační vrstva udržuje vlastní databázi identit, která odkazuje na síťové identity, aniž by poskytovatelům aplikací zpřístupňovala citlivé síťové informace. Když se uživatel autentizuje v aplikaci, ALSI je předána aplikačnímu serveru, který následně komunikuje se síťovými autentizačními funkcemi za účelem ověření identity. Toto ověření může zahrnovat kontrolu stavu předplatného, oprávnění ke službám a další atributy spojené se síťovým předplatným uživatele.

Klíčovými komponentami v ekosystému ALSI jsou aplikační servery, které vydávají a spravují ALSIs, autentizační servery, které tyto identity ověřují proti síťovým záznamům, a databáze mapování identit, které udržují vztahy mezi identifikátory na aplikační a síťové úrovni. Tyto komponenty spolupracují prostřednictvím standardizovaných rozhraní definovaných v specifikacích 3GPP, aby zajistily interoperabilitu mezi implementacemi různých dodavatelů.

V síťové architektuře hraje ALSI klíčovou roli při umožňování nadstavbových služeb tím, že poskytuje trvalou identitu, kterou mohou aplikace používat ke sledování uživatelských relací, preferencí a využívání služeb napříč různými přístupovými metodami. To umožňuje poskytovatelům služeb nabízet personalizované zážitky a zároveň udržovat bezpečnost prostřednictvím síťové autentizace, když je to vyžadováno. Oddělení aplikační identity od síťové identity také posiluje ochranu soukromí tím, že omezuje vystavení síťových identifikátorů poskytovatelům aplikací.

## K čemu slouží

ALSI bylo vytvořeno, aby vyřešilo rostoucí potřebu správy identity na aplikační vrstvě v mobilních sítích s rozšiřováním nadstavbových služeb. Před zavedením ALSI museli poskytovatelé aplikací buď vytvářet vlastní systémy identity (což vedlo k množství přihlašování a špatné uživatelské zkušenosti), nebo spoléhat na síťové identifikátory, jako je [MSISDN](/mobilnisite/slovnik/msisdn/) (což vystavovalo citlivé síťové informace aplikační vrstvě). To vytvářelo bezpečnostní slabiny a omezovalo flexibilitu nabízených služeb.

Primárním motivem pro vývoj ALSI bylo umožnit poskytovatelům služeb nabízet personalizované, bezproblémové zážitky napříč více aplikacemi při zachování správných bezpečnostních hranic mezi síťovou a aplikační vrstvou. Poskytnutím dedikovaného identifikátoru na aplikační úrovni mohly systémy 3GPP podporovat bohatší ekosystémy služeb, kde aplikace mohou udržovat trvalé identity uživatelů bez nutnosti přímého přístupu k síťovým autentizačním mechanismům. Toto oddělení také usnadnilo soulad s regulacemi tím, že omezilo vystavení osobně identifikovatelných informací na síťové úrovni.

Historicky zavedení ALSI ve verzi 4 (Release 4) časově souviselo s rozšiřováním mobilních datových služeb a nástupem sofistikovaných aplikačních platforem. Předchozí přístupy buď nutily poskytovatele aplikací budovat kompletní systémy správy identity (což zvyšovalo složitost a náklady), nebo vyžadovaly použití síťových identifikátorů, které nebyly navrženy pro použití na aplikační vrstvě. ALSI tyto problémy vyřešilo tím, že poskytlo standardizovaný způsob, jak propojit domény identity aplikací a sítě při zachování odpovídajících bezpečnostních kontrol a ochrany soukromí.

## Klíčové vlastnosti

- Identita na aplikační vrstvě oddělená od síťových identifikátorů
- Schopnost mapování na síťové identity pro účely autentizace
- Podpora trvalé identity uživatele napříč aplikačními relacemi
- Standardizovaná rozhraní pro ověřování identity
- Ochrana soukromí omezeným vystavením síťových identifikátorů
- Interoperabilita mezi různými dodavateli aplikací a sítí

## Související pojmy

- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)
- [GUTI – Globally Unique Temporary UE Identity](/mobilnisite/slovnik/guti/)
- [SUPI – Subscription Permanent Identifier](/mobilnisite/slovnik/supi/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [ALSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/alsi/)
