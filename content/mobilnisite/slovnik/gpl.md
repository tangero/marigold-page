---
slug: "gpl"
url: "/mobilnisite/slovnik/gpl/"
type: "slovnik"
title: "GPL – Generic Push Layer"
date: 2025-01-01
abbr: "GPL"
fullName: "Generic Push Layer"
category: "Services"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/gpl/"
summary: "Generic Push Layer (GPL) je standardizovaná servisní vrstva definovaná 3GPP pro zajištění spolehlivého a bezpečného doručování push oznámení a zpráv do mobilních zařízení. Poskytuje společný rámec pro"
---

GPL je standardizovaná servisní vrstva 3GPP, která poskytuje společný rámec pro spolehlivé a bezpečné doručování push oznámení a zpráv do mobilních zařízení, přičemž abstrahuje síťové detaily pro zajištění interoperability.

## Popis

Generic Push Layer (GPL) je vrstva servisních schopností specifikovaná v dokumentu 3GPP TS 33.224. Funguje jako prostředník mezi poskytovateli push služeb (PSP) a infrastrukturou mobilního síťového operátora ([MNO](/mobilnisite/slovnik/mno/)), standardizuje rozhraní a procedury pro doručování push obsahu do uživatelského zařízení (UE). Architektura GPL je navržena jako nezávislá na konkrétní síti, podporuje doručování přes různé přístupové technologie včetně 3G, 4G a 5G. Jejím primárním úkolem je přijímat push požadavky od autorizovaných PSP, tyto požadavky autentizovat a autorizovat a následně spolehlivě přeposlat push obsah do cílového UE pomocí příslušných síťových mechanismů doručení.

V jádru GPL definuje sadu standardizovaných [API](/mobilnisite/slovnik/api/) a protokolů pro komunikaci mezi Push Initiátorem (PI), což je entita PSP, a Push Proxy Gateway (PPG) v doméně MNO. PPG je klíčová síťová funkce, která komunikuje s jádrem sítě, aby lokalizovala účastníka a doručila zprávu. GPL zajišťuje zabezpečenou komunikaci mezi PI a PPG pomocí mechanismů jako je vzájemná autentizace a ochrana integrity zpráv, jak je definováno v bezpečnostních specifikacích. Také řeší aspekty jako formátování zpráv, stanovení priority a hlášení stavu doručení zpět poskytovateli služeb.

Tato vrstva spravuje celý životní cyklus push transakce. Po přijetí push požadavku PPG provede autorizační kontroly účastníka, zjistí stav dosažitelnosti UE (např. připojené, dosažitelné pro push) a vybere optimální metodu doručení. To může zahrnovat spuštění procedur iniciovaných sítí k navázání datového spojení, pokud je UE v režimu nečinnosti. GPL podporuje různé typy push obsahu, včetně oznámení pro probuzení aplikace (např. pro služby rich communication) nebo doručení malých datových přenosů. Její návrh odděluje servisní logiku poskytovatele push služeb od složitostí správy mobility a relací mobilní sítě, čímž poskytuje škálovatelnou a bezpečnou platformu pro služby založené na push mechanismu.

## K čemu slouží

Generic Push Layer byla vytvořena pro řešení roztříštěnosti a nedostatku standardizace v raných mechanismech push oznámení v mobilních sítích. Před zavedením GPL poskytovatelé služeb často spoléhali na proprietární nebo neinteroperabilní metody (jako specifické SMS gatewaye nebo trvalá datová spojení) pro doručování oznámení, což vedlo k nekonzistentní uživatelské zkušenosti, bezpečnostním slabinám a neefektivnímu využívání síťových a zařízení zdrojů. Rozšíření neustále zapnutých aplikací vyžadujících včasné aktualizace (např. e-mail, instant messaging, oznámení aplikací) si vyžádalo síťově efektivní a spolehlivý standard.

GPL tyto problémy řeší tím, že poskytuje jednotné, standardizované rozhraní v rámci architektury 3GPP. Umožňuje jakémukoli autorizovanému poskytovateli služeb spolehlivě kontaktovat zařízení účastníka energeticky efektivním způsobem, využívajíc znalost sítě o stavu účastníka. Tato standardizace snižuje vývojovou složitost pro poskytovatele aplikací a zajišťuje bezpečné, autentizované doručení kontrolované operátorem. Motivací byla potřeba podporovat vznikající IP-based multimediální služby a komunikaci typu stroj-stroj, kde je efektivní komunikace iniciovaná sítí klíčová, aniž by zařízení muselo udržovat konstantní aktivní datové spojení, čímž se šetří životnost baterie zařízení.

## Klíčové vlastnosti

- Standardizované rozhraní (Pp) mezi Push Initiátorem a Push Proxy Gateway
- Podpora zabezpečených, autentizovaných push požadavků od poskytovatelů služeb
- Síťově efektivní správa dosažitelnosti UE a probouzení mechanismů
- Hlášení stavu doručení a potvrzení pro Push Initiátora
- Podpora různých typů push obsahu a úrovní priority
- Autorizace a vynucování politik pro push služby kontrolované operátorem

## Definující specifikace

- **TS 33.224** (Rel-19) — Generic Push Layer (GPL) Specification

---

📖 **Anglický originál a plná specifikace:** [GPL na 3GPP Explorer](https://3gpp-explorer.com/glossary/gpl/)
