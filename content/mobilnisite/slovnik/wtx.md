---
slug: "wtx"
url: "/mobilnisite/slovnik/wtx/"
type: "slovnik"
title: "WTX – Waiting Time eXtension"
date: 2025-01-01
abbr: "WTX"
fullName: "Waiting Time eXtension"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/wtx/"
summary: "Mechanismus prodloužení časovače používaný ve WAP Push, který umožňuje uživateli více času na reakci na indikaci služby. Zabrání předčasnému vypršení push zprávy, když je uživatel upozorněn, ale potře"
---

WTX je mechanismus prodloužení časovače ve WAP Push, který zabraňuje předčasnému vypršení push zprávy a poskytuje uživateli více času na reakci na indikaci služby.

## Popis

Waiting Time eXtension (WTX) je specifický mechanismus definovaný v rámci frameworku Wireless Application Protocol ([WAP](/mobilnisite/slovnik/wap/)) Push, který je součástí Push Access Protocol ([PAP](/mobilnisite/slovnik/pap/)). Není to samostatný protokol, ale parametr nebo funkce používaná během push transakce. Hlavní scénář zahrnuje Push Initiator (např. obsahový server) odesílající push zprávu, konkrétně Service Indication ([SI](/mobilnisite/slovnik/si/)), k WAP klientovi přes Push Proxy Gateway (PPG). SI typicky obsahuje krátkou zprávu a [URI](/mobilnisite/slovnik/uri/); po přijetí klientské zařízení upozorní uživatele (např. pomocí vyskakovacího okna nebo zvuku) a čeká, až se uživatel rozhodne, zda aktivuje (načte) obsah z poskytnutého URI.

Klíčový problém, který WTX řeší, je správa 'čekací doby' během této uživatelské interakce. Původní push odeslání od Push Initiator k PPG obsahuje parametr nazvaný 'Push Expiration Time', který definuje maximální dobu života push zprávy v síti. Samostatně, když PPG doručí SI klientovi, zahrne parametr 'Client Wait Time', který klientovi udává, jak dlouho má čekat na reakci uživatele na upozornění, než bude push interakce považována za vypršenou. Pokud uživatel nereaguje během této Client Wait Time, klient může upozornění zahodit. Uživatel však může upozornění vidět, ale potřebovat více času na rozhodnutí nebo na získání stabilního připojení před aktivací.

Mechanismus WTX umožňuje WAP klientovi požádat PPG o prodloužení této čekací doby. Když se počáteční Client Wait Time blíží vypršení a uživatel stále nezareagoval, ale klient chce udržet upozornění aktivní (např. uživatel ho viděl, ale nezamítl), může klient odeslat zpět k PPG zprávu WTX request. Tato žádost požaduje konkrétní časové prodloužení. PPG po přijetí platné WTX žádosti může prodloužení udělit odpovědí s novým, pozdějším časem vypršení. Tento proces efektivně obnoví 'nájem' push transakce, zabrání předčasnému vypršení indikace služby a dá uživateli více času na akci, aniž by bylo nutné, aby serverový Push Initiator znovu odeslal celou push zprávu. Je to uživatelsky orientovaná funkce, která zlepšuje použitelnost push služeb v mobilním prostředí, kde může být pozornost uživatele přerušovaná.

## K čemu slouží

WTX byl vytvořen, aby vyřešil specifický problém použitelnosti v servisním modelu [WAP](/mobilnisite/slovnik/wap/) Push, zejména pro Service Indications. Na starších mobilních zařízeních byl výpočetní výkon a plocha obrazovky omezená a uživatelé mohli být přerušeni během jiných činností. Standardní push model měl rigidní časovou strukturu: síť (PPG) držela zprávu po určitou dobu a klient zobrazoval upozornění po pevnou dobu trvání časovače na straně klienta. Pokud byl uživatel upozorněn, ale potřeboval více času na rozhodnutí (např. během schůzky, při řízení nebo z důvodu dočasné ztráty signálu), upozornění mohlo zmizet a příležitost snadno přistoupit k nabízenému obsahu by byla ztracena, což by potenciálně vyžadovalo, aby server zprávu odeslal znovu.

Toto omezení degradovalo uživatelský zážitek u časově citlivých, ale ne okamžitých push služeb, jako jsou novinkové upozornění, aktualizace skóre nebo notifikace e-mailů. Mechanismus WTX poskytl elegantní způsob, jak prodloužit interaktivní okno bez zapojení původního Push Initiator, čímž se snížila signalizace v síti a zatížení serveru. Bral v potaz kontext mobilního použití, kde okamžitá akce není vždy možná nebo žádoucí. Tím, že umožnil klientovi vyjednat více času přímo s PPG, učinil push službu flexibilnější a uživatelsky přívětivější, čímž zvýšil pravděpodobnost zapojení uživatele s nabízeným obsahem. Řešil nesoulad mezi časovači vypršení na síťové úrovni a reálnými časy lidské reakce.

## Klíčové vlastnosti

- Umožňuje WAP klientovi požádat o prodloužení Client Wait Time pro čekající Service Indication
- Vyjednávání probíhá přímo mezi klientem a Push Proxy Gateway (PPG), bez zapojení Push Initiator
- Zabraňuje předčasnému vypršení uživatelských notifikací, čímž zlepšuje použitelnost služby
- Používá specifické řídicí zprávy v rámci frameworku protokolu WAP Push
- Pomáhá šetřit síťové prostředky tím, že se vyhne zbytečným retransmisím push zpráv ze serveru
- Zlepšuje uživatelský zážitek u interaktivních push služeb na omezených mobilních zařízeních

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [WTX na 3GPP Explorer](https://3gpp-explorer.com/glossary/wtx/)
