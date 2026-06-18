---
slug: "rhi"
url: "/mobilnisite/slovnik/rhi/"
type: "slovnik"
title: "RHI – Response Header Identifier"
date: 2002-01-01
abbr: "RHI"
fullName: "Response Header Identifier"
category: "Protocol"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/rhi/"
summary: "Protokolový prvek definovaný v 3GPP TS 23.048 pro prostředí pro provádění aplikací v mobilní stanici (MExE). Identifikuje typ hlavičky v odpovědní zprávě serveru směrem k mobilnímu zařízení. To umožňu"
---

RHI je protokolový prvek ve specifikaci MExE, který identifikuje typ hlavičky v odpovědní zprávě serveru, aby umožnil strukturované poskytování a správu služeb.

## Popis

Identifikátor hlavičky odpovědi (Response Header Identifier, RHI) je specifické pole v rámci protokolového rámce MExE, standardizované ve 3GPP Release 5. MExE poskytuje standardizované prováděcí prostředí na mobilních zařízeních, umožňující bezpečné stahování a provádění aplikací. RHI funguje v rámci struktury zpráv vyměňovaných mezi serverem MExE (často platformou poskytovatele služeb) a klientem MExE v uživatelském zařízení (UE). Jeho primární funkcí je signalizovat typ následujících informací hlavičky v odpovědní zprávě, což umožňuje klientovi správně zpracovat a interpretovat odpověď serveru.

Technicky je RHI kódový bod neboli identifikátor v rámci jednotky protokolových dat ([PDU](/mobilnisite/slovnik/pdu/)). Když klient MExE odešle požadavek (např. na aktualizaci konfigurace služby, stažení aplikace nebo vyjednávání schopností), server formuluje odpověď. Tato odpověď je strukturována s hlavičkami obsahujícími řídicí informace a tělem s hlavním datovým obsahem. Pole RHI je jedním z prvních zpracovávaných prvků a udává formát a sémantiku následujících polí hlavičky. Může například rozlišovat mezi hlavičkou obsahující bezpečnostní přihlašovací údaje, příkazem pro správu relace nebo informacemi o chybě.

Role RHI je klíčová pro interoperabilitu a robustní doručování služeb. Poskytnutím jasného, standardizovaného identifikátoru zajišťuje, že různé implementace klientů a serverů MExE mohou vzájemně jednoznačně rozumět svým zprávám. Funguje ve spojení s dalšími protokolovými prvky, jako je Délka hlavičky odpovědi (Response Header Length, [RHL](/mobilnisite/slovnik/rhl/)), což umožňuje klientovi vypočítat přesnou velikost sekce hlavičky před jejím zpracováním. Tento strukturovaný přístup předchází chybám při parsování, zvyšuje bezpečnost tím, že zajišťuje správnou interpretaci dat, a podporuje dynamické služební prostředí, pro které byl MExE navržen. Jeho specifikace v TS 23.048 jej řadí mezi základní komponenty mechanismů MExE pro vyjednávání schopností služeb a výměnu dat.

## K čemu slouží

RHI byl vytvořen jako součást specifikací MExE, aby řešil potřebu flexibilního, ale zároveň strukturovaného protokolu pro správu mobilních aplikací a služeb. Před standardizovanými prováděcími prostředími bylo poskytování služeb často závislé na konkrétním dodavateli, což vedlo k fragmentaci a omezené interoperabilitě. MExE si kladlo za cíl vytvořit univerzální platformu pro stahovatelné aplikace, koncepčně podobnou apletu Java, ale pro mobilní doménu. Klíčovou výzvou bylo navržení komunikačního protokolu, který by dokázal podporovat různé typy služeb – od jednoduchých aktualizací konfigurace po složité stahování aplikací – a zároveň zůstal efektivní přes omezená rádiová rozhraní.

Zavedení RHI vyřešilo problém nejednoznačnosti zpráv v odpovědích serveru. Bez standardizovaného identifikátoru by klient musel spoléhat na pevné formáty zpráv nebo signalizaci mimo pásmo, aby porozuměl obsahu odpovědi, což by činilo protokol nepružným a obtížně rozšiřitelným. RHI umožňuje protokolu být rozšiřitelným; nové typy hlaviček lze definovat v budoucích specifikacích a přiřadit jim nové hodnoty RHI, zatímco starší klienti mohou stále zpracovávat zprávy tím, že identifikují a případně ignorují neznámé typy hlaviček (pokud to protokol umožňuje). Tato dopředná kompatibilita byla klíčová pro dlouhodobý vývoj mobilních služeb. Jeho vytvoření bylo motivováno širší vizí 3GPP v Release 5, která měla umožnit bohatší, stahovatelné služby na sítích 3G, a posunout se tak za hranice jednoduchého hlasu a [SMS](/mobilnisite/slovnik/sms/) směrem k programovatelnému mobilnímu internetu.

## Klíčové vlastnosti

- Identifikuje typ a strukturu polí hlavičky v odpovědní zprávě serveru MExE.
- Umožňuje jednoznačné parsování a interpretaci jednotek protokolových dat klientem MExE.
- Spolupracuje s délkou hlavičky odpovědi (Response Header Length, RHL) pro přesné vymezení rámce zprávy.
- Podporuje rozšiřitelnost protokolu tím, že umožňuje definované kódové body pro nové typy hlaviček.
- Usnadňuje interoperabilitu mezi různými implementacemi klientů a serverů MExE.
- Nedílná součást procedur MExE pro vyjednávání schopností služeb a stahování dat.

## Související pojmy

- [RHL – Response Header Length](/mobilnisite/slovnik/rhl/)

## Definující specifikace

- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management

---

📖 **Anglický originál a plná specifikace:** [RHI na 3GPP Explorer](https://3gpp-explorer.com/glossary/rhi/)
