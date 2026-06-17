---
slug: "mmsr"
url: "/mobilnisite/slovnik/mmsr/"
type: "slovnik"
title: "MMSR – Multimedia Messaging Service Recipient"
date: 2025-01-01
abbr: "MMSR"
fullName: "Multimedia Messaging Service Recipient"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mmsr/"
summary: "Multimedia Messaging Service Recipient (MMSR) je uživatelské zařízení nebo aplikace, která přijímá a zpracovává zprávy služby multimediálních zpráv (MMS). Jedná se o klíčovou funkční entitu v architek"
---

MMSR je uživatelské zařízení nebo aplikace, která přijímá a zpracovává zprávy služby multimediálních zpráv (MMS).

## Popis

Multimedia Messaging Service Recipient (MMSR) je logická funkční entita definovaná ve specifikacích 3GPP pro službu multimediálních zpráv ([MMS](/mobilnisite/slovnik/mms/)). Představuje koncový bod, který přijímá a spotřebovává MMS zprávy. V praktických nasazeních je MMSR typicky implementována jako software na uživatelském zařízení (UE), například jako aplikace pro zasílání zpráv v mobilním telefonu, nebo jako klientská aplikace na zařízení. MMSR komunikuje s prostředím služby multimediálních zpráv ([MMSE](/mobilnisite/slovnik/mmse/)) za účelem stažení zpráv, které jí byly doručeny.

Architektonicky je MMSR součástí MMS uživatelského agenta (MMS UA) na straně příjemce. Když je MMS zpráva odeslána, je nejprve předána do centra služby multimediálních zpráv (MMSC) prostřednictvím MMS uživatelského agenta odesílatele. MMSC následně upozorní MMSR zamýšleného příjemce na čekající zprávu, typicky prostřednictvím WAP push přes řídicí kanál, jako je SMS. Po přijetí tohoto upozornění MMSR naváže datové spojení (např. přes paketové přenosy) a stáhne skutečný obsah zprávy z MMSC pomocí protokolů jako [HTTP](/mobilnisite/slovnik/http/) nebo WAP. MMSR musí podporovat potřebné kodeky a mediální formáty, aby mohla zobrazit přijatý multimediální obsah.

Klíčové součásti funkčnosti MMSR zahrnují obslužný program pro upozornění, klienta pro stahování a engine pro vykreslování médií. MMSR musí také spravovat uživatelské preference, jako je nastavení automatického stahování, a zpracovávat doručovací zprávy zpět k odesílateli. Její fungování je standardizováno, aby byla zajištěna interoperabilita napříč různými sítěmi a výrobci zařízení. MMSR hraje zásadní roli v modelu ukládání a přeposílání MMS, což zajišťuje spolehlivé doručování zpráv i v případě, kdy je zařízení příjemce dočasně nedostupné.

## K čemu slouží

MMSR byla vytvořena jako součást standardizace služby multimediálních zpráv ([MMS](/mobilnisite/slovnik/mms/)) v 3GPP za účelem definování jasného a interoperabilního koncového bodu pro příjem multimediálních zpráv. Před MMS bylo zasílání zpráv většinou omezeno na text (SMS), který nepodporoval obrázky, audio ani video. Vzestup sítí 2,5G a 3G s jejich vylepšenými datovými schopnostmi vytvořil příležitost pro poutavější službu zasílání zpráv. Specifikace MMSR vyřešila problém, jak tyto multimediální zprávy spolehlivě doručovat a zobrazovat na široké škále uživatelských zařízení.

Standardizací role příjemce zajistilo 3GPP, že MMS zpráva odeslaná ze zařízení v síti jednoho operátora může být úspěšně přijata a zobrazena na zařízení od jiného výrobce v síti jiného operátora. Tato interoperabilita byla klíčová pro rozšířené přijetí MMS. Entita MMSR abstrahuje složitost stahování médií a jejich vykreslování a poskytuje konzistentní uživatelský zážitek. Vyřešila tak omezení proprietálních řešení pro multimediální zprávy, která nebyla interoperabilní, a umožnila tak globální, standardizovanou službu pro mobilní multimediální komunikaci.

## Klíčové vlastnosti

- Přijímá upozornění na čekající MMS zprávy prostřednictvím WAP push nebo podobných mechanismů
- Iniciuje stažení obsahu MMS zprávy z MMSC pomocí protokolů HTTP nebo WAP
- Dekóduje a vykresluje multimediální obsah (např. obrázky, audio, video) na základě podporovaných formátů
- Generuje a odesílá doručovací zprávy a zprávy o přečtení zpět odesílateli zprávy
- Spravuje uživatelsky konfigurovatelná nastavení pro automatické nebo ruční stahování zpráv
- Spolupracuje se standardizovanými rozhraními MMSC, aby byla zajištěna kompatibilita napříč sítěmi

## Související pojmy

- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)

## Definující specifikace

- **TS 32.270** (Rel-19) — MMS Charging Management Specification
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)

---

📖 **Anglický originál a plná specifikace:** [MMSR na 3GPP Explorer](https://3gpp-explorer.com/glossary/mmsr/)
